<template>
    <div class="header">
        <h2>Manage Bookings</h2>
        <el-button type="primary" >New Booking</el-button>
    </div>
    <div class="main-content">
        <el-table :data="bookings" style="width: 100%">
            <el-table-column prop="room_name" label="Room"/>
            <el-table-column prop="customer_name" label="Customer" />
            <el-table-column prop="start_date_string" label="Check-In" />
            <el-table-column prop="end_date_string" label="Check-Out" />
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

const bookings = ref([])
onMounted(() => {
    axios
        .get("http://127.0.0.1:8000/bookings/")
        .then(response => {
            bookings.value = response.data;
            console.log(bookings.value);
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