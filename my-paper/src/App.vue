<template>
  <el-container style="height: 100vh">
    <el-aside width="300px">
      <MySidebar />
    </el-aside>
    <el-container>
      <ChatBox />
    </el-container>
  </el-container>
</template>

<script>
import MySidebar from './components/MySidebar.vue';
import ChatBox from './components/ChatBox.vue';

export default {
  components: {
    MySidebar,
    ChatBox,
  },
};
</script>

<style>
body,
html,
#app {
  height: 100%;
  margin: 0;
}
</style>
