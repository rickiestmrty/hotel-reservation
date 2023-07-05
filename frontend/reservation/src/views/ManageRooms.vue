<template>
    <div class="header">
        <h2>Manage Rooms</h2>
        <el-button type="primary" >New Room</el-button>
    </div>
    <div class="main-content">
        <el-table :data="rooms" style="width: 100%">
            <el-table-column prop="name" label="Name"/>
            <el-table-column prop="type" label="Type" />
            <el-table-column prop="price" label="Price" />
            <el-table-column fixed="right" width="120">
            <template #default>
                <el-button link type="primary" size="small"
                >View Detail</el-button>
            </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

const rooms = ref([])
onMounted(() => {
    axios
        .get("http://127.0.0.1:8000/rooms/")
        .then(response => {
            rooms.value = response.data;
            console.log(rooms.value);
        })
})

</script>



<style scoped>
.header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 50px;
}

.main-content{
    min-height: 300px;
}
</style>