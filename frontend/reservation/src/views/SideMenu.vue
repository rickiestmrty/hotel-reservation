<template>
  <!-- <el-menu
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
  </el-menu> -->
  <el-menu 
    class="SideMenu"
    active-text-color="#409EFF"
    text-color="#909399"
    background-color="#FFFFFF"
    :router="true">
  
    <router-link to="/">
      <el-menu-item index="1">
        <el-icon><Avatar /></el-icon>
        <template #title>Reserve Guest</template>
      </el-menu-item>
    </router-link>
    <router-link to="/rooms">
      <el-menu-item index="2">
        <el-icon><Room /></el-icon>
        <template #title>Rooms</template>
      </el-menu-item>
    </router-link>
    <router-link to="/bookings">
      <el-menu-item index="3">
        <el-icon><Calendar /></el-icon>
        <template #title>Bookings</template>
      </el-menu-item>
    </router-link>
  </el-menu>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import {
  Avatar,
  OfficeBuilding as Room,
  Calendar,
} from '@element-plus/icons-vue'
</script>


<style scoped>
.SideMenu{
    width: fit-content;
}

el-menu-item {
  display: flex;
  align-items: center;
  gap: 2px;
  
}

el-icon{
  height: auto;
  width: 50px;
}

</style>