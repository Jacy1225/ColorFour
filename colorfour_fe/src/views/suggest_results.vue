<template>
  <div>
    <div id="header"></div>
    <main class="container">
      <div class="row">
        <div v-for="(recommendation, index) in recommendations" :key="index" class="col-4">
          <div class="card" :class="{ selected: selectedIndex === index }">
            <img :src="recommendation.imgSrc" class="card-img-top" :alt="recommendation.altText" />
            <div class="card-body text-center">
              <h5 class="card-title">{{ recommendation.altText }}</h5>
              <button class="btn btn-primary" @click="selectRecommendation(index)">選擇</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row my-4">
        <div class="col-12 text-center">
          <button class="btn btn-primary" @click="submitSelection" @change="handleImageUpload">確認送出</button>
        </div>
      </div>
    </main>
    <div id="footer"></div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "suggest_results",
    data() {
      return {
        recommendations: [
          { id: 1, imgSrc: new URL("@/assets/img/suggest_05.png", import.meta.url).href, altText: "展覽裝" },
          { id: 2, imgSrc: new URL("@/assets/img/suggest_02.png", import.meta.url).href, altText: "展覽裝" },
          { id: 3, imgSrc: new URL("@/assets/img/suggest_04.png", import.meta.url).href, altText: "展覽裝" },
        ],
        selectedIndex: null,
      };
    },
    methods: {
      selectRecommendation(index) {
        this.selectedIndex = index;
      },
      async submitSelection() {
        if (this.selectedIndex !== null) {
          const selectedRecommendation = this.recommendations[this.selectedIndex];

          const payload = {
            recommendation_name: selectedRecommendation.altText,
            recommendation_image: selectedRecommendation.imgSrc,
            location: "美術館",
            occasion: "秋天,休閒,旅行",
            skin_tone: "淡妝",
            closet_want: "長袖T恤,洋裝",
            closet_not_want: "羽絨外套",
          };

          console.log("提交的資料：", payload);

          try {
            const response = await axios.post("http://localhost:8000/recommender/recommendations/", payload, {
              headers: { Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}` },
            });
            console.log("儲存成功：", response.data);
            alert("推薦已儲存成功！");
            this.$router.push("/suggest_index");
          } catch (error) {
            console.error("儲存失敗：", error.response ? error.response.data : error);
            alert("儲存失敗，請稍後再試。");
          }
        } else {
          alert("請選擇一個推薦方案！");
        }
      },
    },
  };
</script>

<style scoped>
  .card.selected {
    border: 2px solid #ff5555;
    box-shadow: 0 0 10px rgba(255, 123, 255, 0.5);
  }
</style>
