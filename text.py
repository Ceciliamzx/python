from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import time
import random
from abc import ABC, abstractmethod


# 数据模型
@dataclass
class UserRequest:
    """用户请求数据结构"""
    destination: str
    start_date: str
    end_date: str
    travelers: int
    budget: float
    interests: List[str]
    special_requests: Optional[str] = None


@dataclass
class HotelBooking:
    """酒店预订信息"""
    hotel_name: str
    location: str
    price_per_night: float
    check_in: str
    check_out: str
    booking_id: str
    amenities: List[str]


@dataclass
class TransportInfo:
    """交通信息"""
    type: str  # flight, train, car, etc.
    provider: str
    departure: str
    destination: str
    departure_time: str
    arrival_time: str
    price: float
    booking_id: str


@dataclass
class RestaurantBooking:
    """餐厅预订信息"""
    restaurant_name: str
    cuisine: str
    location: str
    date: str
    time: str
    party_size: int
    booking_id: str
    price_estimate: float


@dataclass
class ItineraryItem:
    """行程项目"""
    day: int
    date: str
    activities: List[str]
    transport: Optional[TransportInfo] = None
    accommodation: Optional[HotelBooking] = None
    dining: Optional[RestaurantBooking] = None


@dataclass
class Itinerary:
    """完整行程"""
    destination: str
    start_date: str
    end_date: str
    items: List[ItineraryItem]
    total_estimated_cost: float
    notes: Optional[str] = None


@dataclass
class Message:
    """代理间消息格式"""
    sender: str
    recipient: str
    content: Any
    message_type: str
    timestamp: float = time.time()


# 基础代理类
class Agent(ABC):
    """所有代理的基类"""

    def __init__(self, name: str):
        self.name = name
        self.inbox: List[Message] = []
        self.outbox: List[Message] = []

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

    @abstractmethod
    def process_messages(self):
        """处理收到的消息，子类必须实现"""
        pass


# 具体代理实现
class UserAgent(Agent):
    """用户交互代理，负责接收和解析用户请求"""

    def __init__(self):
        super().__init__("user_agent")
        self.user_request: Optional[UserRequest] = None

    def get_user_input(self) -> UserRequest:
        """获取用户输入（实际应用中可以是GUI或CLI输入）"""
        print("\n===== 旅行规划助手 =====")
        destination = input("请输入目的地: ")
        start_date = input("请输入出发日期 (YYYY-MM-DD): ")
        end_date = input("请输入返回日期 (YYYY-MM-DD): ")
        travelers = int(input("请输入旅行人数: "))
        budget = float(input("请输入预算金额: "))
        interests = input("请输入您感兴趣的活动 (用逗号分隔): ").split(',')
        special_requests = input("有什么特殊要求吗? (可选): ")

        self.user_request = UserRequest(
            destination=destination.strip(),
            start_date=start_date.strip(),
            end_date=end_date.strip(),
            travelers=travelers,
            budget=budget,
            interests=[i.strip() for i in interests],
            special_requests=special_requests.strip() if special_requests else None
        )
        return self.user_request

    def process_messages(self):
        """处理收到的消息（主要是来自其他代理的回复）"""
        for message in self.inbox:
            if message.message_type == "itinerary_proposal":
                print("\n===== 您的旅行计划已生成 =====")
                itinerary: Itinerary = message.content
                print(f"目的地: {itinerary.destination}")
                print(f"日期: {itinerary.start_date} 至 {itinerary.end_date}")
                print(f"预计总费用: {itinerary.total_estimated_cost:.2f} 元")
                print("\n每日行程:")
                for item in itinerary.items:
                    print(f"\n第 {item.day} 天 ({item.date}):")
                    print(f"  住宿: {item.accommodation.hotel_name if item.accommodation else '未安排'}")
                    print(f"  交通: {item.transport.provider if item.transport else '未安排'}")
                    print(f"  餐饮: {item.dining.restaurant_name if item.dining else '未安排'}")
                    print("  活动:")
                    for activity in item.activities:
                        print(f"    - {activity}")

                # 询问用户是否确认
                confirm = input("\n是否确认此行程? (y/n): ")
                self.send_message(
                    recipient="coordinator_agent",
                    content={"confirmed": confirm.lower() == 'y'},
                    message_type="itinerary_confirmation"
                )

            elif message.message_type == "booking_confirmation":
                print(f"\n===== 预订确认 =====")
                print(f"{message.content}")

        # 清空收件箱
        self.inbox.clear()


class CoordinatorAgent(Agent):
    """协调代理，负责协调各个专业代理"""

    def __init__(self):
        super().__init__("coordinator_agent")
        self.user_request: Optional[UserRequest] = None
        self.hotel_booking: Optional[HotelBooking] = None
        self.transport_info: List[TransportInfo] = []
        self.restaurant_bookings: List[RestaurantBooking] = []
        self.itinerary: Optional[Itinerary] = None

    def process_messages(self):
        """处理收到的消息并协调各代理工作"""
        for message in self.inbox:
            # 处理用户请求
            if message.message_type == "user_request":
                self.user_request = message.content
                print(f"[{self.name}] 收到用户请求，开始协调各代理工作")

                # 向各专业代理发送用户需求
                self.send_message(
                    recipient="hotel_agent",
                    content=self.user_request,
                    message_type="hotel_request"
                )
                self.send_message(
                    recipient="transport_agent",
                    content=self.user_request,
                    message_type="transport_request"
                )
                self.send_message(
                    recipient="restaurant_agent",
                    content=self.user_request,
                    message_type="restaurant_request"
                )
                self.send_message(
                    recipient="itinerary_agent",
                    content=self.user_request,
                    message_type="itinerary_request"
                )

            # 处理酒店预订结果
            elif message.message_type == "hotel_booking":
                self.hotel_booking = message.content
                print(f"[{self.name}] 收到酒店预订信息")

                # 将酒店信息转发给行程规划代理
                self.send_message(
                    recipient="itinerary_agent",
                    content=self.hotel_booking,
                    message_type="hotel_info"
                )

            # 处理交通信息
            elif message.message_type == "transport_info":
                self.transport_info = message.content
                print(f"[{self.name}] 收到交通信息")

                # 将交通信息转发给行程规划代理
                self.send_message(
                    recipient="itinerary_agent",
                    content=self.transport_info,
                    message_type="transport_info"
                )

            # 处理餐厅预订
            elif message.message_type == "restaurant_bookings":
                self.restaurant_bookings = message.content
                print(f"[{self.name}] 收到餐厅预订信息")

                # 将餐厅信息转发给行程规划代理
                self.send_message(
                    recipient="itinerary_agent",
                    content=self.restaurant_bookings,
                    message_type="restaurant_info"
                )

            # 处理行程规划结果
            elif message.message_type == "itinerary_proposal":
                self.itinerary = message.content
                print(f"[{self.name}] 收到行程规划")

                # 将行程提议发送给用户代理
                self.send_message(
                    recipient="user_agent",
                    content=self.itinerary,
                    message_type="itinerary_proposal"
                )

            # 处理用户确认
            elif message.message_type == "itinerary_confirmation":
                confirmation = message.content
                if confirmation["confirmed"]:
                    print(f"[{self.name}] 行程已确认，开始完成所有预订")
                    # 通知各代理完成最终预订
                    self.send_message(
                        recipient="hotel_agent",
                        content="confirm",
                        message_type="confirm_booking"
                    )
                    self.send_message(
                        recipient="transport_agent",
                        content="confirm",
                        message_type="confirm_booking"
                    )
                    self.send_message(
                        recipient="restaurant_agent",
                        content="confirm",
                        message_type="confirm_booking"
                    )

                    # 向用户发送最终确认
                    self.send_message(
                        recipient="user_agent",
                        content="所有预订已确认，您的旅行计划已安排妥当！",
                        message_type="booking_confirmation"
                    )
                else:
                    print(f"[{self.name}] 行程未被确认，需要重新规划")
                    # 可以在这里添加重新规划的逻辑
                    self.send_message(
                        recipient="user_agent",
                        content="我们将根据您的反馈重新规划行程，请提供更多信息。",
                        message_type="booking_cancellation"
                    )

        # 清空收件箱
        self.inbox.clear()


class HotelAgent(Agent):
    """酒店代理，负责搜索和预订酒店"""

    def __init__(self):
        super().__init__("hotel_agent")
        self.available_hotels: List[Dict] = self._load_hotel_data()
        self.proposed_booking: Optional[HotelBooking] = None

    def _load_hotel_data(self) -> List[Dict]:
        """加载酒店数据（实际应用中会从API或数据库获取）"""
        return [
            {
                "name": "海滨度假酒店",
                "location": "市中心",
                "price_per_night": 800,
                "amenities": ["游泳池", "健身房", "早餐"]
            },
            {
                "name": "城市商务酒店",
                "location": "商业区",
                "price_per_night": 650,
                "amenities": ["免费WiFi", "早餐", "停车场"]
            },
            {
                "name": "经济型旅馆",
                "location": "郊区",
                "price_per_night": 350,
                "amenities": ["免费WiFi", "停车场"]
            }
        ]

    def find_suitable_hotels(self, request: UserRequest) -> List[Dict]:
        """根据用户需求寻找合适的酒店"""
        # 简单的筛选逻辑，实际应用中会更复杂
        nightly_budget = request.budget / ((self._days_between(request.start_date, request.end_date)) * 2)
        return [h for h in self.available_hotels if h["price_per_night"] <= nightly_budget]

    def _days_between(self, start_date: str, end_date: str) -> int:
        """计算两个日期之间的天数"""
        # 简化实现，实际应使用datetime
        return 5  # 假设5天行程

    def propose_booking(self, request: UserRequest) -> HotelBooking:
        """提出酒店预订建议"""
        suitable_hotels = self.find_suitable_hotels(request)
        if not suitable_hotels:
            suitable_hotels = self.available_hotels  # 如果没有符合预算的，返回所有

        # 选择第一个合适的酒店
        hotel = suitable_hotels[0]
        booking_id = f"hotel_{random.randint(1000, 9999)}"

        return HotelBooking(
            hotel_name=hotel["name"],
            location=hotel["location"],
            price_per_night=hotel["price_per_night"],
            check_in=request.start_date,
            check_out=request.end_date,
            booking_id=booking_id,
            amenities=hotel["amenities"]
        )

    def process_messages(self):
        """处理收到的消息"""
        for message in self.inbox:
            if message.message_type == "hotel_request":
                request: UserRequest = message.content
                self.proposed_booking = self.propose_booking(request)

                # 回复协调代理
                self.send_message(
                    recipient="coordinator_agent",
                    content=self.proposed_booking,
                    message_type="hotel_booking"
                )

            elif message.message_type == "confirm_booking":
                # 确认预订
                if self.proposed_booking:
                    print(f"[{self.name}] 已确认酒店预订: {self.proposed_booking.hotel_name}")

        # 清空收件箱
        self.inbox.clear()


class TransportAgent(Agent):
    """交通代理，负责安排交通"""

    def __init__(self):
        super().__init__("transport_agent")
        self.transport_options: List[Dict] = self._load_transport_data()
        self.proposed_transport: List[TransportInfo] = []

    def _load_transport_data(self) -> List[Dict]:
        """加载交通数据（实际应用中会从API或数据库获取）"""
        return [
            {
                "type": "flight",
                "provider": "东方航空",
                "price_range": (800, 1500)
            },
            {
                "type": "train",
                "provider": "高铁",
                "price_range": (300, 800)
            },
            {
                "type": "car",
                "provider": "租车服务",
                "price_range": (200, 500)
            }
        ]

    def propose_transport(self, request: UserRequest) -> List[TransportInfo]:
        """提出交通方案"""
        transport_list = []
        # 为简化，假设提供往返交通
        for transport in self.transport_options[:2]:  # 取前两种交通方式
            # 根据预算选择价格
            price = min(transport["price_range"][1], request.budget / 4)
            price = max(transport["price_range"][0], price)

            # 去程
            departure_time = f"{request.start_date} 09:00"
            arrival_time = f"{request.start_date} 11:30"
            booking_id = f"{transport['type']}_out_{random.randint(1000, 9999)}"

            transport_list.append(TransportInfo(
                type=transport["type"],
                provider=transport["provider"],
                departure="出发地",
                destination=request.destination,
                departure_time=departure_time,
                arrival_time=arrival_time,
                price=price,
                booking_id=booking_id
            ))

            # 返程
            departure_time = f"{request.end_date} 16:00"
            arrival_time = f"{request.end_date} 18:30"
            booking_id = f"{transport['type']}_in_{random.randint(1000, 9999)}"

            transport_list.append(TransportInfo(
                type=transport["type"],
                provider=transport["provider"],
                departure=request.destination,
                destination="出发地",
                departure_time=departure_time,
                arrival_time=arrival_time,
                price=price,
                booking_id=booking_id
            ))

        return transport_list

    def process_messages(self):
        """处理收到的消息"""
        for message in self.inbox:
            if message.message_type == "transport_request":
                request: UserRequest = message.content
                self.proposed_transport = self.propose_transport(request)

                # 回复协调代理
                self.send_message(
                    recipient="coordinator_agent",
                    content=self.proposed_transport,
                    message_type="transport_info"
                )

            elif message.message_type == "confirm_booking":
                # 确认交通预订
                if self.proposed_transport:
                    print(f"[{self.name}] 已确认所有交通预订")

        # 清空收件箱
        self.inbox.clear()


class RestaurantAgent(Agent):
    """餐厅代理，负责预订餐厅"""

    def __init__(self):
        super().__init__("restaurant_agent")
        self.restaurants: List[Dict] = self._load_restaurant_data()
        self.proposed_bookings: List[RestaurantBooking] = []

    def _load_restaurant_data(self) -> List[Dict]:
        """加载餐厅数据"""
        return [
            {
                "name": "海鲜餐厅",
                "cuisine": "海鲜",
                "location": "海滨区",
                "price_range": (150, 300)
            },
            {
                "name": "当地特色菜馆",
                "cuisine": "地方菜",
                "location": "老城区",
                "price_range": (100, 200)
            },
            {
                "name": "意大利餐厅",
                "cuisine": "意大利菜",
                "location": "市中心",
                "price_range": (200, 400)
            },
            {
                "name": "快餐店",
                "cuisine": "快餐",
                "location": "商业区",
                "price_range": (50, 100)
            }
        ]

    def propose_restaurants(self, request: UserRequest) -> List[RestaurantBooking]:
        """根据行程提议餐厅预订"""
        # 简单实现，假设每天安排一个餐厅
        days = 5  # 假设5天行程
        daily_budget = request.budget / (days * 3)  # 假设餐费占预算的1/3

        bookings = []
        # 从餐厅中选择合适的
        suitable_restaurants = [r for r in self.restaurants if r["price_range"][1] <= daily_budget * request.travelers]

        for i in range(days):
            if not suitable_restaurants:
                suitable_restaurants = self.restaurants  # 如果没有符合预算的，返回所有

            # 随机选择一个餐厅
            restaurant = random.choice(suitable_restaurants)
            # 避免重复选择同一餐厅
            suitable_restaurants.remove(restaurant)

            date = f"2023-07-{10 + i}"  # 简单的日期生成
            booking_id = f"rest_{random.randint(1000, 9999)}"

            bookings.append(RestaurantBooking(
                restaurant_name=restaurant["name"],
                cuisine=restaurant["cuisine"],
                location=restaurant["location"],
                date=date,
                time="19:00",
                party_size=request.travelers,
                booking_id=booking_id,
                price_estimate=restaurant["price_range"][1] * request.travelers
            ))

        return bookings

    def process_messages(self):
        """处理收到的消息"""
        for message in self.inbox:
            if message.message_type == "restaurant_request":
                request: UserRequest = message.content
                self.proposed_bookings = self.propose_restaurants(request)

                # 回复协调代理
                self.send_message(
                    recipient="coordinator_agent",
                    content=self.proposed_bookings,
                    message_type="restaurant_bookings"
                )

            elif message.message_type == "confirm_booking":
                # 确认餐厅预订
                if self.proposed_bookings:
                    print(f"[{self.name}] 已确认所有餐厅预订")

        # 清空收件箱
        self.inbox.clear()


class ItineraryAgent(Agent):
    """行程规划代理，负责制定详细行程"""

    def __init__(self):
        super().__init__("itinerary_agent")
        self.user_request: Optional[UserRequest] = None
        self.hotel_info: Optional[HotelBooking] = None
        self.transport_info: List[TransportInfo] = []
        self.restaurant_info: List[RestaurantBooking] = []
        self.attractions: List[Dict] = self._load_attractions()

    def _load_attractions(self) -> List[Dict]:
        """加载景点数据"""
        return [
            {"name": "博物馆", "type": "文化"},
            {"name": "海滩", "type": "自然"},
            {"name": "购物中心", "type": "购物"},
            {"name": "历史古迹", "type": "文化"},
            {"name": "国家公园", "type": "自然"},
            {"name": "主题公园", "type": "娱乐"},
            {"name": "当地市场", "type": "购物"},
            {"name": "艺术画廊", "type": "文化"}
        ]

    def create_itinerary(self) -> Itinerary:
        """创建行程"""
        if not all([self.user_request, self.hotel_info, self.transport_info, self.restaurant_info]):
            raise ValueError("缺少必要信息，无法创建行程")

        # 简单实现，假设5天行程
        days = 5
        itinerary_items = []

        # 根据用户兴趣筛选景点
        filtered_attractions = self.attractions
        if self.user_request.interests:
            filtered_attractions = [a for a in self.attractions
                                    if any(interest.lower() in a["type"].lower()
                                           for interest in self.user_request.interests)]

        # 为每天创建行程项目
        for day in range(1, days + 1):
            date = f"2023-07-{10 + day - 1}"  # 简单的日期生成

            # 选择当天活动
            day_activities = []
            for i in range(2):  # 每天2个活动
                if filtered_attractions:
                    attraction = random.choice(filtered_attractions)
                    filtered_attractions.remove(attraction)
                    day_activities.append(f"参观 {attraction['name']} ({attraction['type']})")
                else:
                    day_activities.append("自由活动")

            # 分配交通、住宿和餐饮
            transport = self.transport_info[0] if day == 1 else None  # 第一天有去程交通
            if day == days:
                transport = self.transport_info[1]  # 最后一天有返程交通

            accommodation = self.hotel_info
            dining = self.restaurant_info[day - 1] if day - 1 < len(self.restaurant_info) else None

            itinerary_items.append(ItineraryItem(
                day=day,
                date=date,
                activities=day_activities,
                transport=transport,
                accommodation=accommodation,
                dining=dining
            ))

        # 计算总费用
        total_cost = 0
        if self.hotel_info:
            total_cost += self.hotel_info.price_per_night * days
        total_cost += sum(t.price for t in self.transport_info)
        total_cost += sum(r.price_estimate for r in self.restaurant_info)

        return Itinerary(
            destination=self.user_request.destination,
            start_date=self.user_request.start_date,
            end_date=self.user_request.end_date,
            items=itinerary_items,
            total_estimated_cost=total_cost,
            notes="行程根据您的兴趣和预算定制，祝您旅途愉快！"
        )

    def process_messages(self):
        """处理收到的消息"""
        for message in self.inbox:
            if message.message_type == "itinerary_request":
                self.user_request = message.content

            elif message.message_type == "hotel_info":
                self.hotel_info = message.content

            elif message.message_type == "transport_info":
                self.transport_info = message.content

            elif message.message_type == "restaurant_info":
                self.restaurant_info = message.content

            # 当所有必要信息都收集完毕后，创建行程
            if all([self.user_request, self.hotel_info, self.transport_info, self.restaurant_info]):
                try:
                    itinerary = self.create_itinerary()
                    self.send_message(
                        recipient="coordinator_agent",
                        content=itinerary,
                        message_type="itinerary_proposal"
                    )
                except Exception as e:
                    print(f"[{self.name}] 创建行程时出错: {str(e)}")

        # 清空收件箱
        self.inbox.clear()


# 系统管理类
class TravelPlanningSystem:
    """旅行规划系统，管理所有代理"""

    def __init__(self):
        # 创建所有代理
        self.user_agent = UserAgent()
        self.coordinator_agent = CoordinatorAgent()
        self.hotel_agent = HotelAgent()
        self.transport_agent = TransportAgent()
        self.restaurant_agent = RestaurantAgent()
        self.itinerary_agent = ItineraryAgent()

        # 所有代理的列表
        self.agents = [
            self.user_agent,
            self.coordinator_agent,
            self.hotel_agent,
            self.transport_agent,
            self.restaurant_agent,
            self.itinerary_agent
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
        """运行旅行规划系统"""
        print("欢迎使用智能旅行规划系统！")

        # 获取用户请求
        user_request = self.user_agent.get_user_input()

        # 用户代理发送请求给协调代理
        self.user_agent.send_message(
            recipient="coordinator_agent",
            content=user_request,
            message_type="user_request"
        )

        # 处理消息循环
        max_iterations = 10
        iteration = 0

        while iteration < max_iterations:
            print(f"\n===== 处理轮次 {iteration + 1} =====")

            # 路由消息
            self._route_messages()

            # 每个代理处理自己的消息
            for agent in self.agents:
                agent.process_messages()

            # 检查是否完成
            if hasattr(self.coordinator_agent, 'itinerary') and iteration > 3:
                # 如果已经生成行程并且经过了几个处理轮次，退出
                break

            iteration += 1
            time.sleep(1)  # 简单延迟，便于观察输出


# 运行系统
if __name__ == "__main__":
    system = TravelPlanningSystem()
    system.run()
