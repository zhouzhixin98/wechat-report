<template>
  <div>
    <div class="a">亲爱的懒懒懒，我们在一起了一年啦~~</div>
    <div class="b">年年有你，岁岁有我</div>
    <div class="c">出发去看看我们的过去的一年~</div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.a,
.b,
.c {
  text-align: center;
  color: white;
}
.a {
  font-size: 8vw;
  padding-top: 15vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: .5s;
  animation-fill-mode: backwards;
}
.b {
  font-size: 6vw;
  padding-top: 15vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}
.c {
  font-size: 5vw;
  font-weight: lighter;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1.5s;
  animation-fill-mode: backwards;
}
</style>