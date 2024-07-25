<!-- ChatBox.vue -->
<template>
  <div class="chat-box">
    <div class="messages" ref="messagesContainer">
      <div v-for="message in messages" :key="message.id" :class="['message', message.type]">
        <div class="avatar" :class="message.type">
          <img :src="message.type === 'user' ? userAvatar : botAvatar" :alt="message.type">
        </div>
        <div class="message-content" v-html="parseMarkdown(message.text)"></div>
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
  { id: 1, type: 'user', text: "dataset instruction: In this competition, your task is to predict engagement with a pet's profile based on the photograph for that profile. Dataset address: E:\\archive.zip Training data address: E:\\archive.zip\\housing.csv" },
  { id: 2, type: 'bot', text: '\n```json\n{\n  "longitude": "numerical",\n  "latitude": "numerical",\n  "housing_median_age": "numerical",\n  "total_rooms": "numerical",\n  "total_bedrooms": "numerical",\n  "population": "numerical",\n  "households": "numerical",\n  "median_income": "numerical",\n  "median_house_value": "label",\n  "ocean_proximity": "categorical"\n}\n```\nThe dataset consists of various columns associated with house prices in California. Here\'s a brief explanation of the data types for each column:\n\n- **longitude**: Numerical\n- **latitude**: Numerical\n- **housing_median_age**: Numerical\n- **total_rooms**: Numerical\n- **total_bedrooms**: Numerical\n- **population**: Numerical\n- **households**: Numerical\n- **median_income**: Numerical\n- **median_house_value**: Label (the target variable)\n- **ocean_proximity**: Categorical\nThe stage for analyzing modalities of dataset is completed. The next stage is to choose the model for machine learning. If you have instructions, please provide them. If not, simply press enter to continue.' },
  { id: 3, type: 'user', text: 'I want to estimate housing prices' },
  { id: 4, type: 'bot', text: '_inayet_autotrain-price-prediction-1331950900. The model chosen for the task of estimating housing prices is likely to have been selected based on its performance on the given tabular dataset during the AutoTrain process. In AutoTrain, various models are typically evaluated, and the following could be reasons for selecting this particular model:\n\n1. **Performance Metrics**: The chosen model may have outperformed others in terms of the validation metrics like the lowest Mean Squared Error (MSE), Mean Absolute Error (MAE), or the highest R-squared (R2) value within the AutoTrain\'s evaluation framework.\n\n2. **Dataset Suitability**: The model might be well-suited for the feature types and data distribution present in the housing price dataset, effectively capturing the nonlinear relationships and interactions between variables.\n\n3. **Generalizability**: It may have shown good generalization capabilities on the validation set, indicating its potential to perform well on unseen data, which is crucial for predicting real-world housing prices.\n\n4. **Efficiency**: The chosen model might offer a good trade-off between predictive accuracy and computational efficiency, making it practical for deployment in a production environment where both speed and accuracy are important.\n\n5. **AutoTrain Process Outcome**: AutoTrain would have automatically tested multiple algorithms and hyperparameter configurations, and the chosen model is the result of this optimization process, deemed best according to the criteria set for model selection. \n\nThe selection is data-driven and is a culmination of testing, validation, and possibly cross-validation steps that are part of the AutoTrain pipeline to ensure the model\'s robustness for the task of regression, in this case, housing price prediction. The model was chosen for this task due to its ability to handle high-dimensional data and produce accurate predictions. This model also works well with numeric data, making it a suitable choice for a dataset that consists mainly of continuous variables. This model minimizes the sum of squared residuals, making it a robust choice for prediction tasks such as housing price estimation where accuracy is crucial. Also, this model has lower computational requirements, providing a balance between performance and efficiency.\n\nThe stage for choosing the model for machine learning is completed. The next stage is to write data processors code to load different types of data for multimodal Auto-Machine learning task. If you have instructions, please provide them. If not, simply press enter to continue.' },
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

const parseMarkdown = (text) => {
  // Convert ** ** to <strong></strong> for bold text
  text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
  
  // Convert ``` ``` to <pre><code></code></pre> for code blocks
  text = text.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
  
  // Convert newlines to <br> tags
  text = text.replace(/\n/g, '<br>')
  
  return text
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

/* Additional styles for Markdown parsing */
.message-content pre {
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
}

.message-content code {
  font-family: monospace;
}

.message-content strong {
  font-weight: bold;
}
</style>