<template>
  <div id="app">
      <button type="button" class="btn btn-default" @click="toast">click</button>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    toast () {
      this.$toast('操作成功', {
        callback () {
          console.log('结束了')
        },
        type: 'success',
        // position: 'topRight',
        autoClose: false
      })
    }
  }
}
</script>

<style lang="scss">

</style>
