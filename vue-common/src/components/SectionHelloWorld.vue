<!-- components/SectionHelloWorld.vue -->
<template>
  <div class="hello-world">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  props: {
    msg: {
      type: String,
      default: 'Hello Vue + Fast API!'
    }
  }
}
</script>

<style>
#hello-world {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
