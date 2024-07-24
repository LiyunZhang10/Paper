<!-- App.vue -->
<template>
  <el-container class="app-container">
    <el-aside width="250px" class="sidebar">
      <MySidebar />
    </el-aside>
    <el-container class="main-container">
      <el-header class="header">
        <h1>AI Chat Assistant</h1>
      </el-header>
      <el-main>
        <ChatBox />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import MySidebar from './components/MySidebar.vue'
import ChatBox from './components/ChatBox.vue'
</script>

<style>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: 'Arial', sans-serif;
}

#app {
  height: 100%;
}

.app-container {
  height: 100vh;
}

.sidebar {
  background-color: #2c3e50;
  color: white;
}

.main-container {
  background-color: #f0f2f5;
}

.header {
  background-color: #3498db;
  color: white;
  display: flex;
  align-items: center;
  padding: 0 20px;
}
</style>