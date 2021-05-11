# devops-eng-training

## Web service for calculate two numbers

### Abstract
Flask를 이용하여 web service를 만들었다. 기능은 간단하다. 유저로부터 2개의 숫자와 연산자를 받고 결과를 다시 웹에 보여준다. 이번 프로젝트는 기능 보다는 웹 서빙과 Devops에 활용되는 test case를 만드는 것에 의의가 있다. test는 숫자 계산에 대한 case와 웹 서비스가 잘 동작하는지에 대해서 구현하였다. 이 테스트는 향 후 서비스 관리에 이용된다.  
route는 처음에 접속하면 index.html을 rendering한다. 그리고 /get/* 와 같은 형식으로 plus, sub, multiplication, divide 4가지에 경우에 대해서 Get method를 요청하여 input 숫자에 대한 연산을 한다. n1, n2 2개와 각 연산의 버튼을 누르면 결과를 볼 수 있다.

### Usage
```
git clone https://github.com/DaeseungLee/devops-eng-training.git
python3 app.py
```

localhost와 포트번호 5000(default)로 연결되어 크롬과 같은 웹 브라우저로 접속하면 다음과 같은 화면을 볼 수 있다. 화면은 직관적으로 보기 쉬운데, 숫자 2개와 연산 (+,-,*,/) 각각의 출력 버튼을 누르면 최종 결과물을 받아볼 수 있다.

### Test
function 부분은 unittest folder안의 test_functions.py를 통해, web service 부분은 integration folder안의 test_app.py를 통해 test할 수 있다. devops-eng-training 폴더에서 다음 명령어로 각각 실행 할 수 있다.  
  
python3 -m pytest unittest  
python3 -m pytest integration  

각각 구현된 test case 모두 통과하는 것을 볼 수 있다.


