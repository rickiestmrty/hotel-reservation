<template>
  <el-menu
    class="SideMenu"
    active-text-color="#409EFF"
    text-color="#909399"
    background-color="#FFFFFF"
    :router="true"
  >
    <div style="display: flex; align-items: center; justify-content: center">
      <el-button type="text">
        <i class="fa-solid fa-bars"></i>
      </el-button>
    </div>
    <RouterLink to="/">
      <el-menu-item index="/">
        <i class="fa-solid fa-users-rectangle"></i>
        <template #title>Reserve Guest</template>
      </el-menu-item>
    </RouterLink>
  </el-menu>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>


<style scoped>
.SideMenu{
    width: fit-content;
}


</style>