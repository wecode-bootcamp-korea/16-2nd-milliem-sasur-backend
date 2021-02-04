#./Dockerfile
FROM python:3
# 기반이 될 이미지

# 작업 디렉토리(default)설정
WORKDIR /usr/src/app

## Install packages
# 현재 패키지 설치 정보를 도커 이미지에 복사
COPY requirements.txt ./

#설치 정보를 읽어 패키지를 설치 
# 참고로 RUN 명령어는 CMD 명령어와 다르게 container bash안에서 하는 명령이(X)
# 쉽게 밑 작업 해주는 명령어(추측상 docker에서 하는 엔진 명령어 비스무리 한것 같음.
RUN pip install -r requirements.txt


# Copy all src files
# 현재 경로에 존재하는 모든 소스파일을 이미지에 복사 
# ..(X) . .(O) 

COPY . .


# RUN THE APPLICATION ON THE PORT 8000
# 8000번 포트를 외부에 개방하도록 설정함
# 참고로 'EXPOSE 8000 # EXPOSE 뒤에 주석 달면 오류'

EXPOSE 8000

# CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8000"]
# gunicorn을 사용해서 서버를 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "milliem.wsgi:application"]

