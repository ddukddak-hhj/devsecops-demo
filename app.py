# Flask 모듈에서 Flask 클래스를 임포트
from flask import Flask

# Flask 애플리케이션 인스턴스를 생성
# __name__은 현재 파일의 이름으로, 이 값을 통해 Flask가 앱의 위치를 파악함
app = Flask(__name__)

# 라우트(route) 설정: "/" 경로로 접속했을 때 실행될 함수 지정
@app.route("/")
def hello():
    # 웹 브라우저에 표시될 메시지 반환
    return "Hello from DevSecOps!"

# 이 파일이 메인 프로그램으로 실행될 경우
# 0.0.0.0: 모든 네트워크 인터페이스에서 접근 가능
# 5000: Flask의 기본 포트
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
