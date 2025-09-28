# create flask api
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy.util import await_only
from quart import Quart, request, jsonify
from basic.chatai import getLLM, chatGPT, planning_agent

app = Quart(__name__)

# app = Flask(__name__)
# CORS(app)
@app.route('/api/person', methods=['GET'])
def get_person():
    return [1, 2, 3]

@app.route('/api/television', methods=['GET'])
def get_television():
    return [3, 4, 5]

@app.route('/api/chat/<content>', methods=['GET'])
async def chat(content):
    result = await chatGPT(content)
    return result

phone_product_list = [
    {
        "id": 1,
        "name": "iPhone 15 Pro",
        "price": 9999,
        "icon": "https://www.apple.com/v/iphone-15-pro/a/images/overview/hero/hero_iphone_15_pro__d1x4o8x6e6qq_large.jpg"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S23",
        "price": 8999,
        "icon": "https://images.samsung.com/is/image/samsung/p6pim/cn/sm-s9110zkachc/gallery/cn-galaxy-s23-ultra-s911-sm-s9110zkachc-530402530?$720_576_PNG$"
    },
    {
        "id": 3,
        "name": "Google Pixel 7",
        "price": 7999,
        "icon": "https://store.google.com/product/images/phone_pixel_7_colors_just_black.png"
    }
]

@app.route('/api/product/ai_assistance/<user_input>', methods=['GET'])
async def product_consult(user_input):
    user_prompt_template = f"""
    你是一个电商客服，你的任务是根据用户的需求推荐合适
    的手机产品。你有以下的产品列表：
    {phone_product_list}
    请根据用户的需求，推荐最合适的手机产品，并说明理由。
    用户的需求是：{user_input}
    """
    result = await chatGPT(user_prompt_template)
    return result

@app.route('/api/planing_agent/<user_input>', methods=['GET'])
async def agent(user_input):
    user_prompt_template = f"""
    {user_input}
    """
    result = await planning_agent(user_prompt_template)
    return result

if __name__ == '__main__':
    app.run(debug=False)


