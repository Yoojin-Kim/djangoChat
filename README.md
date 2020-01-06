# djangoChat


1) 이용방법

  아래 링크로 접속하시면 확인하실 수 있습니다. 
  
  닉네임 먼저 입력 후 submit 버튼을 눌러주세요. 
  그 다음 원하는 채팅방 이름을 입력 후 Enter 버튼을 누르면 채팅방으로 입장할 수 있습니다. 
  같은 이름의 채팅방에 동시접속 시 다른 이용자와의 채팅이 가능합니다. 



2) 설명

  장고를 처음 다뤄보아서 초반에 기초적인 내용을 학습하고 개발환경을 세팅하느라 시간이 오래 걸렸습니다. 
  이용자 로그인 기능을 구현하고 싶었으나, 시간이 부족하여 닉네임 입력으로 대체하였습니다. 

  초기 화면인 index.html에서는 닉네임을 입력하면 user모델과 연결된 form모델에서 Http Post 메소드를 통해 입력 데이터를 가지고 있습니다. 
  이후 이 데이터를 데이터베이스로 넘깁니다. 
  채팅방 화면인 room.html 에서는 user객체들에 접근하여, 가장 최근에 입력한 이름을 가져옵니다. 
  이는 웹소켓의 통신방식과는 다릅니다. 
  (이용자가 채팅방에 입장하면 이 이름과 함께 입장했다는 메세지가 나옵니다.) 
  채팅방에서 메세지를 전송할 때는 이용자가 입력한 텍스트와 함께 해당 이용자의 닉네임, 메세지, 입력한 시간을 모두 전송하고 이를 화면에 띄웁니다. 
  따라서 이용자들은 서로를 닉네임으로 구분할 수 있고, 메세지를 입력한 시간도 알 수 있습니다. 
  웹소켓의 db는 redis를 사용하였습니다. 
  
  배포는 ~~를 사용하였습니다. WSGI 와 ASGI 의 두 가지 방식을 가능하게 배포하는 것이 어려웠습니다. 


시간이 부족하여 로그인 기능을 구현하지 못한 점이 아쉬웠고, 디자인도 조금 아쉽습니다. 
그렇지만 channels 라이브러리를 통해 채팅 어플리케이션을 구현해본 것은 흥미로웠고, 
처음 다뤄보는 장고에 대해 익숙해질 수 있었습니다. 

감사합니다!
