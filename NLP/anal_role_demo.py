from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# 模型和分词器路径
MODEL_PATH = "/root/HanLP/ChatGLM3/chatglm3-6b"

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = model.quantize(bits=4).to('cuda').eval()

def load_and_concatenate_text(character_directory):
    """加载所有章节的角色文件并连接文本"""
    all_text = ""
    for root, dirs, files in os.walk(character_directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    all_text += f.read().replace('\n', ' ') + " "
    return all_text

def split_text(text, chunk_size=2000):
    """将文本分割为指定大小的块，准备给模型分批处理"""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def analyze_character(text_chunks, character_name):
    """分析角色特征，文本块分批处理后最后进行综合分析"""
    # 组合输入提示信息
    initial_prompt = (
        f"分析《龙族》系列中的{character_name}角色。"
        "请你分析并总结，从以下四个角度分析这个角色：角色的性格特征、角色在故事中的发展与成长，"
        "角色在故事中的重要程度以及变化，角色自身社会文化背景。"
        "输出必须符合以下格式，并确保每个部分字数不少于100字："
        "角色性格特征：\n角色发展与成长：\n角色在故事中的重要程度：\n角色社会文化背景：\n\n"
    )

    # 连续发送每个文本块
    for chunk in text_chunks:
        input_ids = tokenizer.encode(chunk, return_tensors="pt").to("cuda")
        model.generate(input_ids, max_length=3000, pad_token_id=tokenizer.eos_token_id, do_sample=False)

    # 结束提示，要求综合分析
    final_prompt = f"现在，请综合上述所有内容，详细分析{character_name}的角色特征。"
    input_ids = tokenizer.encode(final_prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(input_ids, max_length=3000, pad_token_id=tokenizer.eos_token_id)
    text_generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return text_generated

def main():
    character_directory = "/root/HanLP/character_analysis"
    character_name = "路明非"  # 这里可以根据实际角色进行修改
    all_text = load_and_concatenate_text(character_directory)
    text_chunks = split_text(all_text, 2000)
    character_analysis = analyze_character(text_chunks, character_name)
    print(character_analysis)

if __name__ == "__main__":
    main()
