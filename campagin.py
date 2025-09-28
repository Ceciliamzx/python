from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import time
import random
import re
from abc import ABC, abstractmethod


# ------------------------------
# 工具模块（Tools）
# ------------------------------
class Tool(ABC):
    """所有工具的基类，定义工具接口"""

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """执行工具功能，子类必须实现"""
        pass


class VenueSearchTool(Tool):
    """场地搜索工具：根据活动需求查找合适场地"""

    def __init__(self):
        # 预设场地数据库
        self.available_venues = [
            {
                "name": "国际会议中心",
                "address": "市中心商务区会议大道1号",
                "capacity": 500,
                "price": 20000,
                "amenities": ["投影设备", "音响系统", "空调", "茶歇服务"],
                "suitable_for": ["会议", "展览", "大型活动"]
            },
            {
                "name": "创意艺术空间",
                "address": "文化创意园区B3栋",
                "capacity": 100,
                "price": 8000,
                "amenities": ["开放式空间", "艺术装饰", "咖啡区", "小型舞台"],
                "suitable_for": ["派对", "小型演出", "创意工作坊", "小型会议"]
            },
            {
                "name": "花园宴会厅",
                "address": "湖畔路88号",
                "capacity": 200,
                "price": 15000,
                "amenities": ["户外花园", "宴会厅", "餐饮服务", "停车区"],
                "suitable_for": ["婚礼", "庆典", "晚宴", "中型会议"]
            },
            {
                "name": "商务中心会议室",
                "address": "金融街15号",
                "capacity": 80,
                "price": 5000,
                "amenities": ["投影", "白板", "咖啡", "高速网络"],
                "suitable_for": ["小型会议", "研讨会", "培训"]
            },
            {
                "name": "科技会展中心",
                "address": "高新技术园区创新路7号",
                "capacity": 300,
                "price": 18000,
                "amenities": ["智能设备", "同声传译", "大型LED屏", "VIP室"],
                "suitable_for": ["技术会议", "产品发布", "行业论坛"]
            }
        ]

    def execute(self, event_type: str, participants: int, budget: float,
                preferences: Optional[Dict] = None, **kwargs) -> List[Dict]:
        """搜索符合条件的场地，支持偏好设置"""
        print(f"[场地搜索工具] 正在为{event_type}搜索合适场地...")

        # 处理偏好设置
        preferences = preferences or {}
        min_capacity = preferences.get('min_capacity', participants)
        max_price = preferences.get('max_price', budget * 0.4)
        required_amenities = preferences.get('required_amenities', [])

        # 搜索类型扩展
        search_types = [event_type]
        if event_type == "会议":
            search_types.extend(["小型会议", "中型会议", "技术会议"])

        # 筛选场地
        suitable_venues = [
            venue for venue in self.available_venues
            if any(t in venue["suitable_for"] for t in search_types)
               and venue["capacity"] >= min_capacity
               and venue["price"] <= max_price
               and all(amenity in venue["amenities"] for amenity in required_amenities)
        ]

        # 按相关性排序（价格、容量匹配度）
        suitable_venues.sort(key=lambda x: (
            abs(x["capacity"] - participants),  # 容量匹配度
            x["price"]  # 价格从低到高
        ))

        if not suitable_venues:
            print(f"[场地搜索工具] 未找到适合{event_type}的场地，请调整需求或预算")
        return suitable_venues


class CopywritingTool(Tool):
    """文案生成工具：根据活动信息生成宣传文案"""

    def execute(self, event_type: str, date: str, time: str, location: str,
                theme: Optional[str] = None, tone: Optional[str] = None, **kwargs) -> Dict:
        """生成活动宣传文案，支持语气调整"""
        print(f"[文案生成工具] 正在生成{event_type}宣传文案...")

        # 根据活动类型确定语气
        tone_map = {
            "会议": "正式专业",
            "派对": "活泼热情",
            "婚礼": "温馨浪漫",
            "展览": "艺术气息",
            "庆典": "热烈欢快"
        }
        current_tone = tone or tone_map.get(event_type, "适中友好")

        # 生成标题
        if theme:
            title = f"{theme} - {event_type}盛典"
        else:
            prefixes = ["精彩", "难忘", "卓越", "盛大"]
            title = f"{random.choice(prefixes)}的{event_type}活动"

        # 生成正文内容
        content = f"诚挚邀请您参加于{date} {time}在{location}举办的{event_type}。"

        # 根据活动类型和语气添加特色内容
        content_base = {
            "会议": "本次活动汇聚行业精英，共同探讨前沿趋势与发展机遇，是交流与合作的绝佳平台。",
            "派对": "现场将有精彩表演、互动游戏和精美礼品，让我们一同度过欢乐时光，留下美好回忆。",
            "婚礼": "见证幸福时刻，分享喜悦心情，诚邀您一同见证这份美好的开始，感受爱情的甜蜜。",
            "展览": "将展示众多精品佳作，带来一场视觉盛宴，让您感受艺术与创意的无限魅力。",
            "庆典": "为庆祝这一特殊时刻，我们准备了丰富的活动和惊喜，期待与您共同分享喜悦。"
        }

        # 根据语气调整内容
        tone_modifiers = {
            "正式专业": "敬请拨冗出席，共襄盛举。",
            "活泼热情": "快来加入我们，一起嗨翻天！",
            "温馨浪漫": "让我们一同感受这份美好与温馨。",
            "简洁明了": "期待您的参与。",
            "隆重盛大": "这将是一场不容错过的盛会，诚邀您的光临。"
        }

        content += content_base.get(event_type, "这将是一次难忘的活动体验，期待您的参与。")
        content += tone_modifiers.get(current_tone, "名额有限，请尽早确认，我们期待您的到来！")

        return {
            "title": title,
            "content": content,
            "tone": current_tone,
            "word_count": len(content)
        }


class PosterDesignTool(Tool):
    """海报设计工具：提供海报设计方案"""

    def execute(self, event_type: str, theme: Optional[str] = None, **kwargs) -> Dict:
        """生成海报设计方案"""
        print(f"[海报设计工具] 正在设计{event_type}海报...")

        # 根据活动类型推荐配色方案
        color_schemes = {
            "会议": ["#2C3E50", "#3498DB", "#ECF0F1"],  # 深蓝、浅蓝、浅灰
            "派对": ["#E74C3C", "#F39C12", "#FFFFFF"],  # 红、橙、白
            "婚礼": ["#E8F4F8", "#FFCAD4", "#5A5A5A"],  # 浅蓝、浅粉、深灰
            "展览": ["#9B59B6", "#3498DB", "#FFFFFF"],  # 紫、蓝、白
            "庆典": ["#F1C40F", "#E67E22", "#FFFFFF"]  # 黄、橙、白
        }

        # 确定海报关键元素
        base_elements = ["活动标题", f"日期: {kwargs.get('date')}",
                         f"时间: {kwargs.get('time')}", f"地点: {kwargs.get('location')}"]

        # 根据活动类型添加特殊元素
        type_elements = {
            "会议": ["主讲嘉宾", "议程亮点"],
            "婚礼": ["新人姓名", "爱情故事"],
            "展览": ["展品预览", "门票信息"],
            "派对": ["活动流程", "着装建议"]
        }
        base_elements.extend(type_elements.get(event_type, []))

        return {
            "title": f"{theme}海报设计" if theme else f"{event_type}海报设计",
            "color_scheme": color_schemes.get(event_type, ["#34495E", "#7F8C8D", "#ECF0F1"]),
            "key_elements": base_elements,
            "size": "A3 (297×420mm)",
            "style": f"{event_type}风格，突出主题，视觉吸引力强"
        }


class AdvertisingTool(Tool):
    """广告渠道推荐工具：推荐合适的宣传渠道"""

    def execute(self, event_type: str, budget: float, **kwargs) -> List[Dict]:
        """推荐广告投放渠道"""
        print(f"[广告推荐工具] 正在为{event_type}推荐投放渠道...")

        # 预设广告渠道数据库
        channels = [
            {
                "name": "社交媒体",
                "platforms": ["微信", "微博", "抖音"],
                "audience_reach": 5000,
                "cost_range": (1000, 3000),
                "effectiveness": "高",
                "suitable_for": ["派对", "展览", "婚礼", "庆典", "会议"]
            },
            {
                "name": "行业网站",
                "platforms": ["专业论坛", "行业门户"],
                "audience_reach": 1000,
                "cost_range": (800, 2000),
                "effectiveness": "中",
                "suitable_for": ["会议", "展览", "培训"]
            },
            {
                "name": "线下海报",
                "platforms": ["社区公告栏", "商场展示区"],
                "audience_reach": 2000,
                "cost_range": (1500, 3500),
                "effectiveness": "中",
                "suitable_for": ["派对", "庆典", "社区活动", "会议"]
            },
            {
                "name": "电子邮件",
                "platforms": ["客户邮件列表", "行业通讯"],
                "audience_reach": 800,
                "cost_range": (500, 1500),
                "effectiveness": "中",
                "suitable_for": ["会议", "展览", "培训"]
            }
        ]

        # 筛选适合的渠道
        ad_budget = budget * 0.15  # 广告预算占总预算15%
        suitable_channels = [
            c for c in channels
            if event_type in c["suitable_for"]
               and (c["cost_range"][0] + c["cost_range"][1]) / 2 <= ad_budget
        ]

        # 格式化输出结果
        return [
            {
                "name": c["name"],
                "platforms": c["platforms"],
                "cost": (c["cost_range"][0] + c["cost_range"][1]) / 2,
                "audience_reach": c["audience_reach"],
                "effectiveness": c["effectiveness"]
            }
            for c in suitable_channels[:3]  # 最多推荐3个渠道
        ]


class PersonnelTool(Tool):
    """人员分工工具：生成活动人员安排方案"""

    def execute(self, event_type: str, participants: int, **kwargs) -> List[Dict]:
        """生成人员分工方案"""
        print(f"[人员分工工具] 正在为{event_type}分配人员...")

        # 基础人员配置
        base_roles = [
            {
                "role": "活动负责人",
                "responsibilities": ["整体协调", "决策", "问题处理"],
                "count": 1,
                "skills": ["组织能力", "沟通能力", "应变能力"]
            }
        ]

        # 根据活动类型添加特定角色
        type_roles = {
            "会议": [
                {"role": "主持人", "responsibilities": ["流程引导", "嘉宾介绍"], "count": 1,
                 "skills": ["口才", "控场能力"]},
                {"role": "技术支持", "responsibilities": ["设备调试", "PPT播放"], "count": 1,
                 "skills": ["设备操作", "故障排除"]}
            ],
            "婚礼": [
                {"role": "婚礼策划师", "responsibilities": ["流程设计", "细节把控"], "count": 1,
                 "skills": ["创意", "细心"]},
                {"role": "摄影摄像师", "responsibilities": ["记录过程", "后期处理"], "count": 2,
                 "skills": ["摄影技术", "审美"]}
            ],
            "派对": [
                {"role": "娱乐主持人", "responsibilities": ["气氛调动", "游戏组织"], "count": 1,
                 "skills": ["活泼", "创意"]},
                {"role": "后勤人员", "responsibilities": ["物资准备", "场地维护"], "count": 2,
                 "skills": ["细心", "行动力"]}
            ]
        }

        # 添加活动类型特定角色
        base_roles.extend(type_roles.get(event_type, [
            {"role": "现场协调", "responsibilities": ["流程把控", "人员调度"], "count": 1,
             "skills": ["组织能力", "应变能力"]}
        ]))

        # 根据参与人数添加接待人员
        reception_count = max(2, participants // 50)  # 每50人至少1名接待
        base_roles.append({
            "role": "接待人员",
            "responsibilities": ["签到引导", "解答疑问"],
            "count": reception_count,
            "skills": ["亲和力", "沟通能力"]
        })

        return base_roles


# 工具注册中心
class ToolRegistry:
    """工具注册中心，管理所有可用工具"""

    def __init__(self):
        self.tools: Dict[str, Tool] = {
            "venue_search": VenueSearchTool(),
            "copywriting": CopywritingTool(),
            "poster_design": PosterDesignTool(),
            "advertising": AdvertisingTool(),
            "personnel": PersonnelTool()
        }

    def get_tool(self, tool_name: str) -> Optional[Tool]:
        """获取工具实例"""
        return self.tools.get(tool_name)


# ------------------------------
# 数据模型
# ------------------------------
@dataclass
class EventRequest:
    """用户活动需求数据结构"""
    event_type: str  # 活动类型：会议、派对、婚礼等
    date: str  # 活动日期 YYYY-MM-DD
    time: str  # 活动时间 HH:MM
    duration: float  # 活动持续时间（小时）
    location: str  # 活动地点（城市）
    participants: int  # 参与人数
    budget: float  # 活动预算
    theme: Optional[str] = None  # 活动主题
    special_requests: Optional[str] = None  # 特殊要求
    modifications: Optional[Dict] = None  # 修改请求


@dataclass
class Message:
    """代理间消息格式"""
    sender: str
    recipient: str
    content: Any
    message_type: str
    timestamp: float = time.time()


# ------------------------------
# 代理类
# ------------------------------
class Agent(ABC):
    """所有代理的基类"""

    def __init__(self, name: str, tool_registry: ToolRegistry):
        self.name = name
        self.inbox: List[Message] = []  # 收件箱
        self.outbox: List[Message] = []  # 发件箱
        self.tool_registry = tool_registry  # 工具注册中心引用

    def receive_message(self, message: Message):
        """接收消息"""
        if message.recipient == self.name or message.recipient == "all":
            self.inbox.append(message)
            print(f"[{self.name}] 收到来自 {message.sender} 的消息: {message.message_type}")

    def send_message(self, recipient: str, content: Any, message_type: str):
        """发送消息"""
        message = Message(
            sender=self.name,
            recipient=recipient,
            content=content,
            message_type=message_type
        )
        self.outbox.append(message)
        print(f"[{self.name}] 发送消息给 {recipient}: {message_type}")

    def call_tool(self, tool_name: str, **kwargs) -> Any:
        """调用工具"""
        tool = self.tool_registry.get_tool(tool_name)
        if tool:
            print(f"[{self.name}] 调用工具: {tool_name}")
            return tool.execute(**kwargs)
        print(f"[{self.name}] 工具 {tool_name} 不存在")
        return None

    @abstractmethod
    def process_messages(self):
        """处理收到的消息，子类必须实现"""
        pass


class UserAgent(Agent):
    """用户交互代理：负责与用户沟通，收集活动需求和反馈"""

    def __init__(self, tool_registry: ToolRegistry):
        super().__init__("user_agent", tool_registry)
        self.event_request: Optional[EventRequest] = None
        self.plan_confirmed = False  # 标记计划是否已确认
        self.modification_requests = {}  # 存储用户的修改请求

    def _validate_time_format(self, time_str: str) -> str:
        """验证并标准化时间格式"""
        # 替换全角冒号为半角
        time_str = time_str.replace('：', ':')
        # 验证时间格式 HH:MM
        if not re.match(r'^\d{2}:\d{2}$', time_str):
            raise ValueError("时间格式不正确，请使用HH:MM格式（例如14:30）")
        # 验证小时和分钟范围
        hours, minutes = map(int, time_str.split(':'))
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            raise ValueError("时间值不正确，小时应为0-23，分钟应为0-59")
        return time_str

    def _validate_date_format(self, date_str: str) -> str:
        """验证日期格式 YYYY-MM-DD"""
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
            raise ValueError("日期格式不正确，请使用YYYY-MM-DD格式（例如2023-12-31）")
        return date_str

    def get_user_input(self) -> EventRequest:
        """获取并验证用户输入的活动需求"""
        print("\n===== 活动策划助手 =====")
        try:
            event_type = input("请输入活动类型 (会议/派对/婚礼/展览/庆典等): ").strip()
            date = self._validate_date_format(input("请输入活动日期 (YYYY-MM-DD): ").strip())
            time_str = self._validate_time_format(input("请输入活动时间 (HH:MM): ").strip())

            self.event_request = EventRequest(
                event_type=event_type,
                date=date,
                time=time_str,
                duration=float(input("请输入活动持续时间 (小时): ").strip()),
                location=input("请输入活动地点 (城市): ").strip(),
                participants=int(input("请输入预计参与人数: ").strip()),
                budget=float(input("请输入活动预算 (元): ").strip()),
                theme=input("请输入活动主题 (可选，直接回车跳过): ").strip() or None,
                special_requests=input("请输入特殊要求 (可选，直接回车跳过): ").strip() or None
            )
            return self.event_request
        except ValueError as e:
            print(f"输入错误: {e}")
            print("请重新输入相关信息...")
            return self.get_user_input()  # 重新获取输入

    def get_modification_input(self) -> Dict:
        """获取用户对计划的修改意见"""
        print("\n===== 请提出您的修改意见 =====")
        modifications = {}

        # 询问是否要修改各个部分
        if input("是否需要修改场地? (y/n): ").lower() == 'y':
            venue_prefs = {}
            print("场地修改选项:")
            if input("  是否需要特定设施? (如投影、WiFi等，直接回车跳过): ").strip():
                venue_prefs['required_amenities'] = input("    请输入所需设施(用逗号分隔): ").strip().split(',')
            if input("  是否需要调整场地预算? (y/n): ").lower() == 'y':
                venue_prefs['max_price'] = float(input("    请输入最大场地预算: ").strip())
            if input("  是否需要调整容纳人数? (y/n): ").lower() == 'y':
                venue_prefs['min_capacity'] = int(input("    请输入最小容纳人数: ").strip())
            modifications['venue'] = venue_prefs

        if input("是否需要修改宣传文案? (y/n): ").lower() == 'y':
            copy_prefs = {}
            print("文案修改选项:")
            new_tone = input("  请选择文案语气(正式专业/活泼热情/温馨浪漫/简洁明了/隆重盛大): ").strip()
            if new_tone:
                copy_prefs['tone'] = new_tone
            new_theme = input("  请输入新的活动主题(直接回车保持不变): ").strip()
            if new_theme:
                copy_prefs['theme'] = new_theme
            modifications['copywriting'] = copy_prefs

        if input("是否需要调整预算分配? (y/n): ").lower() == 'y':
            budget_prefs = {}
            budget_prefs['total'] = float(input("  请输入新的总预算: ").strip())
            modifications['budget'] = budget_prefs

        # 其他可能的修改...

        return modifications if modifications else None

    def process_messages(self):
        """处理收到的消息（主要是活动计划）"""
        for message in self.inbox:
            if message.message_type == "event_plan":
                print("\n===== 您的活动计划已生成 =====")
                print(message.content)

                # 询问用户反馈
                while True:
                    action = input("\n请选择操作 (1-确认计划, 2-修改计划, 3-重新输入需求): ").strip()
                    if action == '1':
                        self.plan_confirmed = True
                        self.send_message(
                            "coordinator_agent",
                            {"confirmed": True},
                            "plan_confirmation"
                        )
                        break
                    elif action == '2':
                        # 获取修改意见并发送
                        modifications = self.get_modification_input()
                        if modifications:
                            self.modification_requests = modifications
                            # 更新事件请求中的修改信息
                            if self.event_request:
                                self.event_request.modifications = modifications
                                self.send_message(
                                    "coordinator_agent",
                                    self.event_request,
                                    "modify_request"
                                )
                        break
                    elif action == '3':
                        # 重新输入需求
                        self.event_request = self.get_user_input()
                        self.send_message(
                            "coordinator_agent",
                            self.event_request,
                            "event_request"
                        )
                        break
                    else:
                        print("无效输入，请选择1、2或3")

        self.inbox.clear()


class CoordinatorAgent(Agent):
    """协调代理：负责协调各专业代理工作，处理修改请求"""

    def __init__(self, tool_registry: ToolRegistry):
        super().__init__("coordinator_agent", tool_registry)
        self.event_request: Optional[EventRequest] = None
        self.subtasks = {
            "venue": False,
            "copywriting": False,
            "poster": False,
            "advertising": False,
            "personnel": False
        }
        self.results: Dict[str, Any] = {}  # 存储各代理返回的结果
        self.plan_confirmed = False  # 标记计划是否已确认
        self.revision_count = 0  # 记录修改次数
        self.max_revisions = 3  # 最大修改次数

    def process_messages(self):
        """处理收到的消息，包括初始请求和修改请求"""
        for message in self.inbox:
            if message.message_type == "event_request":
                # 接收用户需求并分发任务
                self.event_request = message.content
                self.subtasks = {k: False for k in self.subtasks}  # 重置任务状态
                self.results.clear()  # 清空之前的结果
                self.revision_count = 0  # 重置修改次数
                self._dispatch_tasks()

            elif message.message_type == "modify_request":
                # 接收修改请求
                self.event_request = message.content
                self.revision_count += 1
                print(f"[{self.name}] 收到修改请求，正在调整计划 (第{self.revision_count}/{self.max_revisions}次修改)")

                # 根据修改内容决定需要重新执行哪些任务
                modifications = self.event_request.modifications or {}
                tasks_to_update = []

                if 'venue' in modifications:
                    tasks_to_update.append("venue")
                if 'copywriting' in modifications:
                    tasks_to_update.append("copywriting")
                if 'budget' in modifications:
                    # 预算变更影响多个任务
                    self.event_request.budget = modifications['budget']['total']
                    tasks_to_update = ["venue", "advertising", "personnel"]

                # 重置需要更新的任务状态
                for task in tasks_to_update:
                    self.subtasks[task] = False

                # 只重新分发需要更新的任务
                self._dispatch_tasks(tasks_to_update)

            elif message.message_type == "subtask_result":
                # 接收子任务结果
                task_name = message.content["task"]
                self.subtasks[task_name] = True
                self.results[task_name] = message.content["result"]
                self._check_all_tasks_completed()

            elif message.message_type == "plan_confirmation":
                # 接收用户对计划的确认
                self.plan_confirmed = message.content["confirmed"]
                if self.plan_confirmed:
                    print(f"[{self.name}] 活动计划已确认，感谢使用！")
                else:
                    print(f"[{self.name}] 活动计划未确认，等待进一步指示...")

        self.inbox.clear()

    def _dispatch_tasks(self, specific_tasks: Optional[List[str]] = None):
        """向各专业代理分发任务，支持指定特定任务"""
        if not self.event_request:
            return

        print(f"[{self.name}] 开始向各专业代理分发任务...")
        tasks_to_send = specific_tasks if specific_tasks else self.subtasks.keys()

        # 获取修改请求
        modifications = self.event_request.modifications or {}

        for task in tasks_to_send:
            if task == "venue":
                # 如果有场地修改偏好，一起发送
                venue_prefs = modifications.get('venue', {})
                self.send_message(
                    "venue_agent",
                    {
                        "request": self.event_request,
                        "preferences": venue_prefs
                    },
                    "find_venue"
                )
            elif task == "copywriting":
                # 如果有文案修改偏好，一起发送
                copy_prefs = modifications.get('copywriting', {})
                self.send_message(
                    "copy_agent",
                    {
                        "request": self.event_request,
                        "preferences": copy_prefs
                    },
                    "write_copy"
                )
            elif task == "poster":
                self.send_message("poster_agent", self.event_request, "design_poster")
            elif task == "advertising":
                self.send_message("ad_agent", self.event_request, "find_channels")
            elif task == "personnel":
                self.send_message("personnel_agent", self.event_request, "assign_personnel")

    def _check_all_tasks_completed(self):
        """检查所有子任务是否完成，完成则生成最终计划"""
        if all(self.subtasks.values()) and self.event_request:
            print(f"[{self.name}] 所有子任务已完成，开始生成活动计划...")
            plan = self._generate_plan()
            self.send_message("user_agent", plan, "event_plan")

    def _generate_plan(self) -> str:
        """生成最终活动计划文本"""
        if not self.event_request:
            return "无法生成计划：缺少活动需求信息"

        # 安全获取场地信息，处理空列表情况
        venue_results = self.results.get("venue", [])
        has_venue = len(venue_results) > 0

        # 计算总费用
        venue_cost = venue_results[0].get("price", 0) if has_venue else 0
        ad_cost = sum(channel.get("cost", 0) for channel in self.results.get("advertising", []))
        personnel_cost = sum(role.get("count", 0) * 300 for role in self.results.get("personnel", []))  # 每人300元估算
        other_cost = self.event_request.budget * 0.2  # 其他费用
        total_cost = venue_cost + ad_cost + personnel_cost + other_cost

        # 构建计划文本
        plan = [
            f"===== 活动计划 {'(修订版)' if self.revision_count > 0 else ''} =====",
            f"活动类型: {self.event_request.event_type}",
            f"活动主题: {self.event_request.theme or '无'}",
            f"日期时间: {self.event_request.date} {self.event_request.time} (持续 {self.event_request.duration} 小时)",
            f"活动地点: {self.event_request.location}",
            f"参与人数: {self.event_request.participants}人",
            f"修改次数: {self.revision_count}/{self.max_revisions}",
            "\n===== 场地信息 ====="
        ]

        # 处理场地信息
        if has_venue:
            plan.extend([
                f"场地名称: {venue_results[0].get('name', '未确定')}",
                f"场地地址: {venue_results[0].get('address', '未确定')}",
                f"容纳人数: {venue_results[0].get('capacity', '未确定')}",
                f"场地费用: {venue_cost:.2f} 元",
                f"场地设施: {', '.join(venue_results[0].get('amenities', []))}"
            ])
        else:
            plan.extend([
                "警告: 未找到符合条件的场地",
                "建议: 1. 增加活动预算",
                "      2. 减少预计参与人数",
                "      3. 考虑其他类型的活动场地"
            ])

        # 继续添加其他信息
        plan.extend([
            "\n===== 宣传文案 =====",
            f"标题: {self.results.get('copywriting', {}).get('title', '未生成')}",
            f"内容: {self.results.get('copywriting', {}).get('content', '未生成')[:100]}...",
            f"文案语气: {self.results.get('copywriting', {}).get('tone', '未设置')}",
            "\n===== 海报设计 =====",
            f"配色方案: {', '.join(self.results.get('poster', {}).get('color_scheme', ['未确定']))}",
            f"关键元素: {', '.join(self.results.get('poster', {}).get('key_elements', ['未确定']))}",
            "\n===== 广告投放 ====="
        ])

        # 添加广告渠道信息
        ad_channels = self.results.get("advertising", [])
        if ad_channels:
            for channel in ad_channels:
                plan.append(f"- {channel['name']}: 成本 {channel['cost']:.2f} 元, 覆盖 {channel['audience_reach']} 人")
        else:
            plan.append("警告: 未找到合适的广告投放渠道，请增加活动预算")

        # 添加人员分工信息
        plan.append("\n===== 人员安排 =====")
        for role in self.results.get("personnel", []):
            plan.append(f"- {role['role']} ({role['count']}人): {', '.join(role['responsibilities'][:2])}...")

        # 添加预算信息
        plan.append("\n===== 预算信息 =====")
        plan.append(f"场地费用: {venue_cost:.2f} 元")
        plan.append(f"广告费用: {ad_cost:.2f} 元")
        plan.append(f"人员费用: {personnel_cost:.2f} 元")
        plan.append(f"其他费用: {other_cost:.2f} 元")
        plan.append(f"总预算: {total_cost:.2f} 元 (原始预算: {self.event_request.budget:.2f} 元)")

        # 添加预算超支警告
        if total_cost > self.event_request.budget * 1.1:  # 超过10%视为超支
            plan.append("\n警告: 预计总费用超出预算10%以上，建议调整活动方案或增加预算")

        return "\n".join(plan)


class VenueAgent(Agent):
    """场地代理：负责查找合适的活动场地，支持偏好设置"""

    def __init__(self, tool_registry: ToolRegistry):
        super().__init__("venue_agent", tool_registry)

    def process_messages(self):
        """处理场地查询请求，包括可能的偏好设置"""
        for message in self.inbox:
            if message.message_type == "find_venue":
                data = message.content
                req: EventRequest = data["request"]
                preferences = data.get("preferences", {})

                # 调用场地搜索工具，传入偏好设置
                venues = self.call_tool(
                    "venue_search",
                    event_type=req.event_type,
                    participants=req.participants,
                    budget=req.budget,
                    preferences=preferences
                )
                # 返回结果给协调代理
                self.send_message(
                    "coordinator_agent",
                    {"task": "venue", "result": venues},
                    "subtask_result"
                )
        self.inbox.clear()


class CopywritingAgent(Agent):
    """文案代理：负责生成宣传文案，支持语气调整"""

    def __init__(self, tool_registry: ToolRegistry):
        super().__init__("copy_agent", tool_registry)

    def process_messages(self):
        """处理文案撰写请求，包括可能的修改偏好"""
        for message in self.inbox:
            if message.message_type == "write_copy":
                data = message.content
                req: EventRequest = data["request"]
                preferences = data.get("preferences", {})

                # 调用文案生成工具，传入可能的修改偏好
                copy = self.call_tool(
                    "copywriting",
                    event_type=req.event_type,
                    date=req.date,
                    time=req.time,
                    location=req.location,
                    theme=preferences.get('theme', req.theme),
                    tone=preferences.get('tone')
                )
                self.send_message(
                    "coordinator_agent",
                    {"task": "copywriting", "result": copy},
                    "subtask_result"
                )
        self.inbox.clear()


class PosterAgent(Agent):
    """海报代理：负责设计海报方案"""

    def __init__(self, tool_registry: ToolRegistry):
        super().__init__("poster_agent", tool_registry)

    def process_messages(self):
        """处理海报设计请求"""
        for message in self.inbox:
            if message.message_type == "design_poster":
                req: EventRequest = message.content
                # 调用海报设计工具
                design = self.call_tool(
                    "poster_design",
                    event_type=req.event_type,
                    theme=req.theme,
                    date=req.date,
                    time=req.time,
                    location=req.location
                )
                self.send_message(
                    "coordinator_agent",
                    {"task": "poster", "result": design},
                    "subtask_result"
                )
        self.inbox.clear()


class AdvertisingAgent(Agent):
    """广告代理：负责推荐广告投放渠道"""

    def __init__(self, tool_registry: ToolRegistry):
        super().__init__("ad_agent", tool_registry)

    def process_messages(self):
        """处理广告渠道查询请求"""
        for message in self.inbox:
            if message.message_type == "find_channels":
                req: EventRequest = message.content
                # 调用广告推荐工具
                channels = self.call_tool(
                    "advertising",
                    event_type=req.event_type,
                    budget=req.budget
                )
                self.send_message(
                    "coordinator_agent",
                    {"task": "advertising", "result": channels},
                    "subtask_result"
                )
        self.inbox.clear()


class PersonnelAgent(Agent):
    """人员代理：负责活动人员分工安排"""

    def __init__(self, tool_registry: ToolRegistry):
        super().__init__("personnel_agent", tool_registry)

    def process_messages(self):
        """处理人员分工请求"""
        for message in self.inbox:
            if message.message_type == "assign_personnel":
                req: EventRequest = message.content
                # 调用人员分工工具
                personnel = self.call_tool(
                    "personnel",
                    event_type=req.event_type,
                    participants=req.participants
                )
                self.send_message(
                    "coordinator_agent",
                    {"task": "personnel", "result": personnel},
                    "subtask_result"
                )
        self.inbox.clear()


# ------------------------------
# 系统管理
# ------------------------------
class EventPlanningSystem:
    """活动策划系统：管理所有代理和系统流程"""

    def __init__(self):
        # 创建工具注册中心
        self.tool_registry = ToolRegistry()

        # 创建所有代理
        self.agents = [
            UserAgent(self.tool_registry),
            CoordinatorAgent(self.tool_registry),
            VenueAgent(self.tool_registry),
            CopywritingAgent(self.tool_registry),
            PosterAgent(self.tool_registry),
            AdvertisingAgent(self.tool_registry),
            PersonnelAgent(self.tool_registry)
        ]

    def _route_messages(self):
        """路由所有代理的消息"""
        for agent in self.agents:
            # 处理每个代理的发送队列
            for message in agent.outbox:
                # 将消息发送给目标代理
                for recipient_agent in self.agents:
                    recipient_agent.receive_message(message)
            # 清空发送队列
            agent.outbox.clear()

    def run(self):
        """运行交互式活动策划系统"""

        print("===== 欢迎使用智能活动策划系统 =====")
        print("本系统将帮助您策划各类活动，并支持根据您的反馈进行调整\n")

        # 获取用户代理并获取用户请求
        user_agent = next(a for a in self.agents if a.name == "user_agent")
        user_request = user_agent.get_user_input()

        # 用户代理发送请求给协调代理
        user_agent.send_message("coordinator_agent", user_request, "event_request")

        # 处理消息循环，直到用户确认计划或达到最大修改次数
        max_iterations = 30  # 足够多的循环次数以支持多轮交互
        iteration = 0
        while iteration < max_iterations:
            print(f"\n===== 系统处理轮次 {iteration + 1}/{max_iterations} =====")
            self._route_messages()

            # 每个代理处理自己的消息
            for agent in self.agents:
                agent.process_messages()

            # 检查是否用户已确认计划，确认后退出
            if hasattr(user_agent, 'plan_confirmed') and user_agent.plan_confirmed:
                print("\n===== 活动策划完成，感谢使用！ =====")
                break

            # 检查协调代理的修改次数是否已达上限
            coordinator = next(a for a in self.agents if a.name == "coordinator_agent")
            if hasattr(coordinator, 'revision_count') and coordinator.revision_count >= coordinator.max_revisions:
                print("\n===== 已达到最大修改次数，将使用当前计划 =====")
                break

            iteration += 1
            time.sleep(1)  # 简单延迟，便于观察处理过程


# 运行系统
if __name__ == "__main__":
    system = EventPlanningSystem()
    system.run()
