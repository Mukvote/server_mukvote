# MukVote Local server 사용법

### 사용법
```
Step1)[anaconda 로컬 설치](https://travislife.tistory.com/26)
**혹시 안되면 환경변수 잘 해줬는지 확인하기**
conda --version 확인해서 잘 나오면 성공!

Step2) conda create --name mu python=3.6
Step3) conda activate "mu"
터미널에 mu가 왼쪽이나 오른쪽 끝에 보이면 성공!

Step4) 깃허브에서 프레임 코드 가져오고, 필요한 라이브러리 설치
git clone https://github.com/Mukvote/server_mukvote.git
cd server_mukvote
pip install -r requirements.txt

**mysql과 mysqlclient**는 따로 설치 필요. 
아마도 pip install mysql 이나 pip install mysqlclient
안되면 구글링 ㄱ ㄱ , 
[혹시 mysqlclient 에러생기면 확인하기](https://stackoverflow.com/questions/48175057/pip-install-mysqlclient-on-amazon-linux)

Step5)mysql 설치후 로컬 터미널로 접속후, 스키마 하나 만들기
mysql -u root -p
create database "" 아마 이런 명령어 였던걸로 기억...<찾아보세요>
[도움될블로그](https://whitepaek.tistory.com/16)
데이타 그립이나 워크벤치로 연결된거 안에 스키마 확인하면 성공! 

Step6).env파일 만들기 (예시!!) --> 위에 mysql에 스키마 하나 로컬에 구축한 이름, 비번은 본인걸로~
DB_NAME="Mukvote"
DB_USER="root"
DB_PASS="KKkk233400!!"
DB_SERVICE="127.0.0.1"
DB_PORT="3306"

Step7)server_muvote 파일안에서 실행하고, 데이타 그립 확인하면 테이블 생성된거 확인 가능!
Flask db init
Flask db migrate
Flask db upgrade

Step8)서버 키기 [기본환경 구축 드디어 끝!!!!!!!!!!!]
flask run
```

### MukVote ec2-server
```
Step1)ec2서버에 접속후, 똑같이 하면 되여, 하나 다른건 env 파일을 이제 모아꺼랑 연결해서 거기에 스키마 따로 만들어서 사용예정
<서버는 제가 기본 연결은 해두었으나 나중에 지금 로컬에 만든걸로 업데이트 해야되서 파일 건드리지 말아주세요!!!!, 또 연결 삽질 안하고싶어요 ㅠㅠㅠ 제밣  ㅠㅠㅠ>
Step2)ssh -i mukvote.pem ec2-user@3.142.77.126
Step3).env 연결 저장용...
DB_NAME="db_class"
DB_USER="admin"
DB_PASS="~~!!moamoa"
DB_SERVICE="database-moa.czk1xhzbk1gf.us-east-2.rds.amazonaws.com"
DB_PORT="3306"
Step4)계획~ 우선 제 로컬에 기본적으로 할꺼고, 여러분들은 각자의 로컬에서 테스트 하고 저한테 주셔서 합치고 최종을 서버에 올리려고 합니다. 

그럼.. 이 정리로... 다들 삽질 들하고 성공하시길 바래요...

```

+ 코드 수정하면서 서버 돌리고 싶으면 이 명령어도 실행 (=>코드가 수정되면 서버가 자동 reload 된다.)
```
export FLASK_ENV=development
```
