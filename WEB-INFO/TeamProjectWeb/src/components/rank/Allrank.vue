<template>
  <h1>ssss</h1>
</template>

<script>
  export default {
    data () {
      return {
        allRank: []
      }
    },
    mounted () {
      this._getAllRank()
    },
    methods: {
      _getAllRank () {
        this.$http.get('/getAllRank').then(response => {
          console.log(response.data)
        })
      }
    }
  }
</script>
