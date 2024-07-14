<template>
  <el-container class="chat-container">
    <el-header class="chat-header">
      <h2>Chat</h2>
    </el-header>
    <el-main class="chat-main">
      <!-- Message display area (if needed) -->
    </el-main>
    <div class="input-fields">
      <el-input v-model="instruction" placeholder="Enter instruction" :autosize="{ minRows: 4, maxRows: 6 }"
        type="textarea" :class="{ 'is-error': showError && !instruction }"></el-input>
      <el-input v-model="dataset" :autosize="{ minRows: 4, maxRows: 6 }" type="textarea" placeholder="Enter dataset"
        :class="{ 'is-error': showError && !dataset }" style="margin-top: 60px;"></el-input>
      <el-input v-model="traindata" placeholder="Enter traindata" :autosize="{ minRows: 4, maxRows: 6 }" type="textarea"
        :class="{ 'is-error': showError && !traindata }" style="margin-top: 60px;"></el-input>
      <el-row :gutter="20" class="submit-row">
        <el-col :span="24">
          <el-button type="primary" @click="submitForm" class="submit-button">Submit</el-button>
        </el-col>
      </el-row>
    </div>
    <p v-if="showError" class="error-message">Please enter values in all input boxes.</p>
    <el-footer class="chat-footer">
      <div class="input-container">
        <el-input v-model="newMessage" placeholder="Type your message" :prefix-icon="Search"
          @keyup.enter="sendMessage"></el-input>
        <el-button type="primary" :icon="Promotion" circle @click="sendMessage"></el-button>
      </div>
    </el-footer>
  </el-container>
</template>

<script>
import { ref } from 'vue'
import { Search, Promotion } from '@element-plus/icons-vue'

export default {
  name: 'ChatBox',
  setup() {
    const messages = ref([])
    const newMessage = ref('')
    const instruction = ref('')
    const dataset = ref('')
    const traindata = ref('')
    const showError = ref(false)

    const sendMessage = () => {
      if (newMessage.value.trim()) {
        messages.value.push({ id: Date.now(), text: newMessage.value })
        newMessage.value = ''
      }
    }

    const submitForm = () => {
      console.log('Submit button clicked') // Confirm the button click is triggered
      if (!instruction.value || !dataset.value || !traindata.value) {
        showError.value = true
        console.log('Error: Please fill all fields') // Log the error
      } else {
        showError.value = false
        console.log('Form submitted:', {
          instruction: instruction.value,
          dataset: dataset.value,
          traindata: traindata.value
        })
        // Add form submission logic here
      }
    }

    return {
      messages,
      newMessage,
      sendMessage,
      Search,
      Promotion,
      instruction,
      dataset,
      traindata,
      showError,
      submitForm
    }
  }
}
</script>

<style scoped>
.chat-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f0f2f5;
}

.chat-header {
  padding: 20px;
  background-color: #fff;
  border-bottom: 1px solid #ddd;
  height: auto;
  text-align: center;
  font-family: 'Arial', sans-serif;
}

.chat-main {
  flex: 1;
  background-color: #fff;
}

.input-fields {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;

  background-color: #fff;
  border-bottom: 1px solid #ddd;
}

.input-fields .el-input {
  margin-top: 250px;
}

.input-fields .is-error {
  border-color: red;
}

.submit-row {
  margin-top: 50px;
  text-align: center;
}

.submit-button {
  width: 600px;
  max-width: 300px;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.chat-footer {
  padding: 20px;
  background-color: #fff;
  border-top: 1px solid #ddd;
}

.input-container {
  display: flex;
  align-items: center;
}

.input-container .el-input {
  flex: 1;
  margin-right: 10px;
}
</style>
