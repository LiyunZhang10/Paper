<!-- ChatBox.vue -->
<template>
  <div class="chat-box">
    <div class="messages" ref="messagesContainer">
      <div v-for="message in messages" :key="message.id" :class="['message', message.type]">
        <div class="avatar" :class="message.type">
          <img :src="message.type === 'user' ? userAvatar : botAvatar" :alt="message.type">
        </div>
        <div class="message-content">{{ message.text }}</div>
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
import userAvatar from '@/assets/user.png'
import botAvatar from '@/assets/robot.png'

const messages = ref([
  { id: 1, type: 'bot', text: 'Hello! How can I assist you today?' },
  { id: 2, type: 'user', text: 'dataset instruction: In this competition, your task is to predict engagement with a pet\'s profile based on the photograph for that profile.' },
  { id: 3, type: 'user', text: 'Dataset address: E:\\archive.zip' },
  { id: 4, type: 'user', text: 'Training data address: E:\\archive.zip\\housing.csv' },
  { id: 5, type: 'bot', text: 'The dataset consists of various columns associated with house prices in California. Here\'s a brief explanation of the data types for each column:\n\n- longitude: Numerical\n- latitude: Numerical\n- housing_median_age: Numerical\n- total_rooms: Numerical\n- total_bedrooms: Numerical\n- population: Numerical\n- households: Numerical\n- median_income: Numerical\n- median_house_value: Label (the target variable)\n- ocean_proximity: Categorical\n\nThe stage for analyzing modalities of dataset is completed. The next stage is to choose the model for machine learning. If you have instructions, please provide them. If not, simply press enter to continue.' },
  { id: 6, type: 'user', text: 'I want to estimate housing prices' },
  { id: 7, type: 'bot', text: 'Model: _inayet_autotrain-price-prediction-1331950900. The model chosen for the task of estimating housing prices is likely to have been selected based on its performance on the given tabular dataset during the AutoTrain process. This model was chosen for its ability to handle high-dimensional data and produce accurate predictions, especially for datasets consisting mainly of continuous variables. It minimizes the sum of squared residuals, making it robust for prediction tasks such as housing price estimation where accuracy is crucial. Additionally, this model offers a good balance between performance and efficiency.' },
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
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.message {
  display: flex;
  margin-bottom: 20px;
  align-items: flex-start;
}

.message-content {
  padding: 10px;
  border-radius: 8px;
  max-width: 70%;
}

.user {
  flex-direction: row-reverse;
}

.user .message-content {
  background-color: #e6f7ff;
  margin-right: 10px;
}

.bot .message-content {
  background-color: #f4f4f4;
  margin-left: 10px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin: 0 10px;
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.input-area {
  display: flex;
  padding: 20px;
  background-color: #f9f9f9;
  border-top: 1px solid #e0e0e0;
}

.input-area .el-input {
  margin-right: 10px;
}

.el-button {
  flex-shrink: 0;
}
</style>
