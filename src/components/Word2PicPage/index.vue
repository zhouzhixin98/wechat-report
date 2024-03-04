<template>
    <div>
      <div class="a">懒懒懒</div>
      <div class="b">你看这一年的这一些瞬间</div>
      <div class="c">超温馨 劲浪漫</div>
      <div class="human">
      <div class="boy">
        <img class="a" src="@/assets/images/dudu1.png" />
        <img class="b" src="@/assets/images/cloud1.png" />
      </div>
    </div>
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
  .human .boy {
  position: relative;
  top: -40vh;
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
  width: 80vw;
  position: relative;
  left: 20%;
  top: 10vh;
  z-index: 2;
}
.human .boy .b {
  width: 50vw;
  position: relative;
  left: -30vw;
  top: 20vh;
}
  </style>