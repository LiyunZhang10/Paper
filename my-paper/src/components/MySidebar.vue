<template>
  <el-menu :default-active="activeIndex" class="el-menu-vertical-demo" @select="handleSelect">
    <el-menu-item index="1">ChatGPT</el-menu-item>
    <el-submenu index="3">
      <template #title>Previous 7 Days</template>
      <el-menu-item index="3-1">Optimize Vue2 ECharts Code</el-menu-item>
      <el-menu-item index="3-2">AI Model Summarizes Conversations</el-menu-item>
      <el-menu-item index="3-3">Dockerize Chrome and ChromeDriver</el-menu-item>
      <el-menu-item index="3-4">Dockerize Spring Boot Selenium</el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: '1',
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath)
    },
  },
}
</script>

<style scoped>
.el-menu-vertical-demo {
  width: 100%;
  height: 100%;
}
</style>
