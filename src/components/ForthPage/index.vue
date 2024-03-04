<template>
  <div>
    <div class="a">
      这一年 我们说过最长的一句话 <span class="value">{{ content.length }}</span
      >字
    </div>
    <div class="b">
      {{ content.substring(0, 100) }}
    </div>
    <div class="c">...</div>
    <div class="d">
      {{ time }}
    </div>
    <div class="human">
      <div class="boy">
        <img class="a" src="@/assets/images/yt3.png" />
        <img class="b" src="@/assets/images/cloud1.png" />
      </div>
    </div>
  </div>
</template>

<script>
import { longMsg } from "@/data.json";
export default {
  data() {
    return {
      ...longMsg,
    };
  },
};
</script>

<style scoped>
.a {
  font-size: 5vw;
  padding-top: 15vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 0.5s;
  animation-fill-mode: backwards;
}
.b {
  padding-top: 5vh;
  white-space: normal;
  text-overflow: ellipsis;
  overflow: hidden;
  line-height: 2;
  color: ebf45f;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}
.c{
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}
.d {
  text-align: right;
  padding-top: 3vh;
  font-weight: bolder;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1.5s;
  animation-fill-mode: backwards;
}
.human .boy {
  position: relative;
  top: -25vh;
  animation: up-down 2s ease-in-out infinite both;
}
@keyframes up-down {
  0% {
    transform: translateY(1vh);
  }
  50% {
    transform: translateY(0vh);
  }
  100% {
    transform: translateY(1vh);
  }
}
.human .boy .a {
  width: 70vw;
  position: relative;
  left: -20vw;
  top: -15vh;
  z-index: 2;
}
.human .boy .b {
  width: 60vw;
  position: relative;
  left: -5vw;
  top: -30vh;
}
</style>