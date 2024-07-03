css = '''
<style>
.chat-message {
    padding: 10px; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex
}
.chat-message.user {
    
background: hsla(221, 40%, 35%, 1);

background: linear-gradient(45deg, hsla(221, 40%, 35%, 1) 0%, hsla(207, 70%, 39%, 1) 100%);

background: -moz-linear-gradient(45deg, hsla(221, 40%, 35%, 1) 0%, hsla(207, 70%, 39%, 1) 100%);

background: -webkit-linear-gradient(45deg, hsla(221, 40%, 35%, 1) 0%, hsla(207, 70%, 39%, 1) 100%);

filter: progid: DXImageTransform.Microsoft.gradient( startColorstr="#354C7C", endColorstr="#1E6AA7", GradientType=1 );
}
.chat-message.bot {
background: hsla(220, 43%, 47%, 1);

background: linear-gradient(45deg, hsla(220, 43%, 47%, 1) 0%, hsla(350, 42%, 57%, 1) 100%);

background: -moz-linear-gradient(45deg, hsla(220, 43%, 47%, 1) 0%, hsla(350, 42%, 57%, 1) 100%);

background: -webkit-linear-gradient(45deg, hsla(220, 43%, 47%, 1) 0%, hsla(350, 42%, 57%, 1) 100%);

filter: progid: DXImageTransform.Microsoft.gradient( startColorstr="#4567AC", endColorstr="#C06474", GradientType=1 );
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.vectorstock.com/i/500p/67/56/happy-robot-3d-ai-character-chat-bot-mascot-vector-51396756.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/premium-psd/businessman-3d-icon-avatar-people_431668-1289.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''