<template>
  <div>
    <div class="a">宝宝，谢谢你带给我这么多</div>
    <div class="b">情人游天地，日月换行李</div>
    <div class="c">我永远爱你~</div>
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