<template>
  <div>
    <div class="a">
      今年我们一共发了
      <span class="value"> {{ count }} </span>
      条消息
    </div>
    <div class="b">
      其中有
      <span class="value"> {{ imgCount }} </span>
      是图片&nbsp; 其中有
      <span class="value"> {{ voiceCount }} </span>
      是语音&nbsp; 还有甜甜蜜蜜的
      <span class="value"> {{ voiceCount }} </span>
      次语音/视频通话
    </div>
    <div class="c">
      <div v-for="(count, word, index) in loveWord" :key="index">
        说{{ word }} <span class="value"> {{ count }} </span>次
      </div>
      <div>...</div>
    </div>
    <div class="d">但是其实，比起网络<br />我们更喜欢在现实表达爱意！</div>
    <div class="human">
      <div class="boy">
        <img class="a" src="@/assets/images/yt1.png" />
        <img class="b" src="@/assets/images/cloud2.png" />
      </div>
    </div>
  </div>
</template>

<script>
import data from "@/data.json";
export default {
  data() {
    return {
      ...data,
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
  animation-delay: .5s;
  animation-fill-mode: backwards;
}
.b{
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}
.c{
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2s;
  animation-fill-mode: backwards;
}
.d {
  padding-top: 10vh;
  font-size: 5vw;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2.5s;
  animation-fill-mode: backwards;
}
.human .boy {
  position: relative;
  top: -10vh;
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
.human .boy .b {
  width: 50vw;
  position: relative;
  left: 5vw;
  top: -35vh;
}
.human .boy .a {
  width: 40vw;
  position: relative;
  left: 50vw;
  top: -40vh;
  z-index: 2;
}
</style>