<template>
  <div class="chat-container">
    <el-header class="chat-header">Chat</el-header>
    <el-main class="chat-main">
      <!-- 这里可以添加消息显示的逻辑 -->
    </el-main>
    <el-footer class="chat-footer">
      <div class="input-container">
        <el-input
          v-model="newMessage"
          placeholder="Type your message"
          prefix-icon="Search"
          @keyup.enter="sendMessage"
        >
        </el-input>
        <el-button
          type="primary"
          icon="el-icon-s-promotion"
          circle
          @click="sendMessage"
        ></el-button>
      </div>
    </el-footer>
  </div>
</template>

<script>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'

export default {
  setup() {
    const messages = ref([])
    const newMessage = ref('')

    const sendMessage = () => {
      if (newMessage.value.trim()) {
        messages.value.push({ id: Date.now(), text: newMessage.value })
        newMessage.value = ''
      }
    }

    return {
      messages,
      newMessage,
      sendMessage,
      Search
    }
  }
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.chat-header {
  background-color: #f5f5f5;
  text-align: center;
  padding: 10px;
  font-weight: bold;
  font-size: 24px;
}

.chat-main {
  flex-grow: 1;
  overflow-y: auto;
}

.chat-footer {
  background-color: #f5f5f5;
  padding: 20px 0;
}

.input-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 960px;
  height: 64px;
  margin: 0 auto;
}

.el-input {
  width: calc(100% - 70px);
}

.el-input :deep(.el-input__inner) {
  border-radius: 32px;
  height: 64px;
}

.el-button {
  margin-left: 10px;
}
</style>
