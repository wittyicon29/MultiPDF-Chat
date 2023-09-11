css = '''
<style>
  /* Chat Container */
  .chat-container {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }

  /* Chat Message Styles */
  .chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    max-width: 70%;
  }

  .chat-message.user {
    background-color: #2b313e;
    color: #fff;
    justify-content: flex-start;
  }

  .chat-message.bot {
    background-color: #475063;
    color: #fff;
    justify-content: flex-end;
  }

  /* Avatar Styles */
  .chat-message .avatar {
    width: 15%;
    margin-right: 1rem;
  }

  .chat-message .avatar img {
    max-width: 100%;
    max-height: 100%;
    border-radius: 50%;
    object-fit: cover;
  }

  /* Message Styles */
  .chat-message .message {
    flex-grow: 1;
    padding: 0.5rem;
    border-radius: 0.3rem;
  }

  /* User-specific Styling */
  .chat-message.user .message {
    background-color: #2b313e;
  }

  .chat-message.bot .message {
    background-color: #475063;
  }

  /* Hover Effect */
  .chat-message:hover {
    transform: scale(1.02);
    transition: transform 0.2s ease-in-out;
  }

  /* Typing Animation (Bot Only) */
  .bot.typing .message::before {
    content: '';
    display: inline-block;
    width: 8px;
    height: 8px;
    margin-right: 5px;
    background-color: #fff;
    border-radius: 50%;
    animation: typing 1s infinite;
  }

  @keyframes typing {
    0% {
      opacity: 0;
      transform: translateY(3px);
    }
    50% {
      opacity: 1;
    }
    100% {
      opacity: 0;
      transform: translateY(-3px);
    }
  }
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''