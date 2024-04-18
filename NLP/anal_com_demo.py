from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# 模型和分词器路径
MODEL_PATH = "/root/HanLP/ChatGLM3/chatglm3-6b"

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = model.quantize(bits=4).to('cuda').eval()

def analyze_comments(prompt_template, data):
    """根据评论分析小说的评价"""
    # 为当前评论构建完整的提示文本
    prompt = prompt_template.format(data)

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
    outputs = model.generate(input_ids, max_length=3000, pad_token_id=tokenizer.eos_token_id)
    text_generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return text_generated

def process_comments_directory(directory_path, output_directory, prompt_template):
    """处理指定目录下的所有评论文件并保存分析结果到另一个目录"""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # 确保输出目录存在

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):  # 假设评论文件以.txt结尾
            file_path = os.path.join(directory_path, filename)
            output_path = os.path.join(output_directory, filename)  # 使用相同的文件名保存结果
            with open(file_path, "r", encoding="utf-8") as file:
                comments = file.read().replace('\n', ' ')  # 读取文本内容并去除所有换行符
                result = analyze_comments(prompt_template, comments)
                with open(output_path, "w", encoding="utf-8") as output_file:
                    output_file.write(result)
                    print(f"Analysis for {filename} saved to {output_path}")

def main():
    # 定义评论文件所在的目录路径和输出目录路径
    comments_directory = "/root/HanLP/output_comment"
    output_comments_analysis_directory = "/root/HanLP/output_comment_anal"
    prompt_template = (
        "你现在是一个优秀的小说评论分析AI，请分析：这部小说的整体评价好坏，读者情感反馈是否达到预期，情节是否令人满意，角色设定是否得到读者喜爱。"
        "输出应符合以下格式，并确保每个部分字数不少于100字：\n\n"
            "整体分析如下：\n读者情感反馈如下：\n情节满意程度如下：\n角色设定满意程度如下：\n\n{}"
    )
    process_comments_directory(comments_directory, output_comments_analysis_directory, prompt_template)

if __name__ == "__main__":
    main()
