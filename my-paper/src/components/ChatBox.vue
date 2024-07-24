<!-- ChatBox.vue -->
<template>
  <div class="chat-box">
    <div class="messages" ref="messagesContainer">
      <div v-for="message in messages" :key="message.id" :class="['message', message.type]">
        {{ message.text }}
      </div>
    </div>
    <div class="input-area">
      <el-input
        v-model="newMessage"
        placeholder="Type your message"
        @keyup.enter="sendMessage"
      >
        <template #prefix>
          <el-icon><ChatLineRound /></el-icon>
        </template>
      </el-input>
      <el-button type="primary" :icon="Promotion" circle @click="sendMessage"></el-button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick, watch } from 'vue'
import { ChatLineRound, Promotion } from '@element-plus/icons-vue'

const messages = ref([
  { id: 1, type: 'bot', text: 'Hello! How can I assist you today?' }
])
const newMessage = ref('')
const messagesContainer = ref(null)

const sendMessage = () => {
  if (newMessage.value.trim()) {
    messages.value.push({ id: Date.now(), type: 'user', text: newMessage.value })
    newMessage.value = ''
    // Simulate bot response
    setTimeout(() => {
      messages.value.push({ id: Date.now(), type: 'bot', text: 'I received your message. How can I help further?' })
    }, 1000)
  }
}

const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

watch(messages, scrollToBottom)

onMounted(scrollToBottom)
</script>

<style scoped>
.chat-box {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 60px);
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 8px;
  max-width: 70%;
}

.user {
  background-color: #e1f3fb;
  align-self: flex-end;
  margin-left: auto;
}

.bot {
  background-color: #f0f0f0;
  align-self: flex-start;
}

.input-area {
  display: flex;
  padding: 20px;
  background-color: #f9f9f9;
  border-top: 1px solid #eaeaea;
}

.input-area .el-input {
  margin-right: 10px;
}

.el-button {
  flex-shrink: 0;
}
</style>
