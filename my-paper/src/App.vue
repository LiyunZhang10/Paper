<!-- App.vue -->
<template>
  <el-container class="app-container">
    <el-aside width="300px" class="sidebar">
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
  overflow: hidden;
}

.sidebar {
  background-color: #f4f4f4;
  color: #333;
  overflow-y: auto;
}

.main-container {
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
}

.header {
  background-color: #ffffff;
  color: #333;
  display: flex;
  align-items: center;
  padding: 0 20px;
  border-bottom: 1px solid #e0e0e0;
  height: 60px;
}

.el-main {
  padding: 0;
  overflow: hidden;
}
</style>
