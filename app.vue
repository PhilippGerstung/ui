<script setup lang="ts">
const router = useRouter();
const navigate = (to: string) => {
  router.push(to);
};
</script>

<template>
  <div class="main-container">
    <div class="top-bar">
      <el-button-group>
        <el-button round @click="navigateTo('/')">Home</el-button>
        <el-button round @click="navigateTo('/stations')"
          >Tankstellen</el-button
        >
        <el-button round @click="navigateTo('/about')">Über</el-button>
      </el-button-group>
    </div>
    <NuxtPage />
  </div>
</template>

<style lang="scss" scoped>
.main-container {
  width: 100%;
  height: 100%;
}

.tob-bar {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
}
</style>
