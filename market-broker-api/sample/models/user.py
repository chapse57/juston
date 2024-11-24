import time
import threading
from datetime import datetime, timedelta, date

class User:
    def __init__(self, access_token: str, expired_date: date, access_token_type: str, expires_in: int):
        self.access_token = access_token
        self.expired_date = expired_date
        self.access_token_type = access_token_type
        self.expires_in = expires_in
        self.stop_event = threading.Event()
        self.refresh_thread = threading.Thread(target=self.refresh_access_token)

    def __repr__(self):
        return (f"User(access_token={self.access_token}, expired_date={self.expired_date}, "
                f"access_token_type={self.access_token_type}, expires_in={self.expires_in})")

    def start_refresh(self):
        self.refresh_thread.start()

    def refresh_access_token(self):
        while not self.stop_event.is_set():
            time_to_wait = self.expires_in - 60  # 1분 전에 리프레시
            time.sleep(time_to_wait)
            self.request_access_token()

    def request_access_token(self):
        # 여기에 액세스 토큰을 요청하는 로직을 추가하세요.
        print(f"Access token refreshed at {datetime.now()}")
        # 새로운 액세스 토큰과 만료 정보를 업데이트
        self.access_token = "new_access_token"  # 실제로는 API 호출로 얻은 토큰
        self.expired_date = datetime.now() + timedelta(seconds=self.expires_in)
        print(self)

    def stop_refresh(self):
        self.stop_event.set()
        self.refresh_thread.join()


# 사용 예시
user = User("initial_token", datetime.now() + timedelta(seconds=3600), "Bearer", 3600)
user.start_refresh()

# 프로그램이 종료될 때까지 대기 (예: 24시간)
try:
    time.sleep(24 * 3600)  # 24시간 대기
finally:
    user.stop_refresh()
