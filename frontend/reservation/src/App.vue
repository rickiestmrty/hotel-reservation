<template>
  <div>
    <el-container class="common-layout">

      <el-header class="header">
        <div class="header-left-side">
          <img alt="Vue logo" class="logo" src="@/assets/Logo.png" width="125" height="125" />
          <h1>N and F Guest House</h1>
        </div>
        <div class="header-right-side">hello</div>
      </el-header>

      <el-container class="layout-container">
        <div class="empty-container"></div>
        <el-aside width="200px"><SideMenu /></el-aside>
        <el-container class="main-container">
          <el-main><RouterView /></el-main>
          <el-footer>Footer</el-footer>
        </el-container>
        <div class="empty-container"></div>
      </el-container>
    </el-container>
  </div>

  

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import SideMenu from './views/SideMenu.vue';

</script>

<style scoped>
/* Set height and width of the root element */
html, body {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}

/* Set full height for the container */
.common-layout {
  height: auto;
  width: 100%;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
}

/* Set full width and position the header at the top */
el-header {
  width: 100%;
  height: 100px;
  position: static;
  top: 0;
  left: 0;
  background-color: #fff;
  z-index: 1;
  display: flex;
  justify-content: space-around;
  flex-wrap: nowrap;
  align-items: center;
}

/* Position the header elements */
.header-left-side {
  display: flex;
  align-items: center;
}

.header-right-side{
}

/* Style the logo */
.logo {
  margin-right: 10px;
}

/* Set the aside width and style */
el-aside {
  width: 15%;
  padding-top: 20px;
  padding-right: 20px;
}

/* Style the main container */
.main-container {
  display: flex;
  flex-direction: column;
  flex: 1;
  
}

/* Set the main content to grow and occupy remaining space */
el-main {
  flex: 1;
  background-color: rgb(141, 42, 91);
}

/* Style the footer */
el-footer {
  margin-top: 10px;
  background-color: rgb(36, 177, 36);
}

.layout-container {
  height: 100%;
  display: flex;
  position: static;
}

/* Center the content in the layout container */
.el-container {
  margin: auto;
}

.empty-container{
  width: 15%;
}


</style>

