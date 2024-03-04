<template>
    <!-- <div class="test">第一次陪你过生日</div> -->
    <div class="box">
      <div class="title">
        <div class="a">你的超级好运横财</div>
      </div>
      <div class="human">
        <div class="boy">
          <img class="a responsive-image" src="@/assets/images/hc1.jpg" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import data from "@/data.json";
  export default {
    data() {
      const { loveWord, mostWord, monthGroup } = data;
      let max = monthGroup[0];
      for (let i of monthGroup) {
        if (i[1] > max[1]) {
          max = i;
        }
      }
      let lc = {
        w: "",
        c: 0,
      };
      Object.keys(loveWord).forEach((key) => {
        const count = loveWord[key];
        if (count > lc.c) {
          lc = {
            w: key,
            c: count,
          };
        }
      });
  
      let mc = {
        w: "",
        c: 0,
      };
  
      Object.keys(mostWord).forEach((key) => {
        const count = mostWord[key];
        if (count > mc.c) {
          mc = {
            w: key,
            c: count,
          };
        }
      });
      return {
        a: mc.w,
        b: lc.w,
        c: max[0],
      };
    },
  };
  </script>
  
  <style scoped>
  .responsive-image {
    max-width: 100%; /* 图片的最大宽度为父容器的100% */
    max-height: auto; /* 图片的最大高度为自动，保持原始宽高比例 */
  }
  </style>