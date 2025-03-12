from smolagents import OpenAIServerModel

model = OpenAIServerModel(
    model_id="deepseek-r1-distill-qwen-7b",
    api_base="http://127.0.0.1:1234/v1",
    api_key='lm-studio',
)