from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 路径定义
MODEL_PATH = "/root/HanLP/ChatGLM3/chatglm3-6b"

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = model.quantize(bits=4).to('cuda').eval()

def analyze_comments(data):
    """
    根据评论分析小说的评价、情感反馈、情节和角色设定。
    Args:
        data (str): 评论数据字符串。
    Returns:
        str: 分析结果。
    """
    # 分析提示文本
    prompt = (
        "请基于以下评论分析这本小说的整体评价好坏，读者情感反馈是否达到预期，"
        "情节是否令人满意，角色设定是否得到读者喜爱。如果没有足够的评论去分析，请直接推测生成。"
        "避免使用'我们推测'、'我们可以假设'等词句，改为'依据评论可看出'。"
        "输出格式：\n"
        "整体分析如下：\n"
        "读者情感反馈如下：\n"
        "情节满意程度如下：\n"
        "角色设定满意程度如下：\n\n"
        "评论内容： \"{}\"".format(data)
    )
    
    # 将提示文本编码为模型能理解的格式
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
    
    # 使用模型生成响应
    outputs = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    
    # 将生成的标记解码为字符串
    text_generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # 清除包含原始评论的部分
    result_section = text_generated.split('评论内容：')[0]
    
    return result_section

def main():
    # 读取评论数据
    comments_path = "/root/HanLP/output_comment/8662633103586503.txt"  # 更新为实际评论文件的路径
    with open(comments_path, "r", encoding="utf-8") as file:
        comments = file.read()

    # 对评论进行分析
    result = analyze_comments(comments)
    
    # 打印分析结果
    print(result)

if __name__ == "__main__":
    main()
