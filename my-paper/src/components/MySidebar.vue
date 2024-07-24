<!-- MySidebar.vue -->
<template>
  <el-menu
    :default-active="activeIndex"
    class="sidebar-menu"
    @select="handleSelect"
    background-color="#2c3e50"
    text-color="#ffffff"
    active-text-color="#ffd04b"
  >
    <el-menu-item index="1">
      <el-icon><ChatLineRound /></el-icon>
      <span>ChatGPT</span>
    </el-menu-item>
    <el-sub-menu index="2">
      <template #title>
        <el-icon><Calendar /></el-icon>
        <span>Previous 7 Days</span>
      </template>
      <el-menu-item index="2-1">Optimize Vue2 ECharts Code</el-menu-item>
      <el-menu-item index="2-2">AI Model Summarizes Conversations</el-menu-item>
      <el-menu-item index="2-3">Dockerize Chrome and ChromeDriver</el-menu-item>
      <el-menu-item index="2-4">Dockerize Spring Boot Selenium</el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script setup>
import { ref } from 'vue'
import { ChatLineRound, Calendar } from '@element-plus/icons-vue'

const activeIndex = ref('1')

const handleSelect = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
.sidebar-menu {
  height: 100%;
}

.sidebar-menu .el-menu-item,
.sidebar-menu .el-sub-menu__title {
  display: flex;
  align-items: center;
}

.sidebar-menu .el-icon {
  margin-right: 10px;
}
</style>