<template>
  <div>
    <div id="header"></div>
    <main class="main-content container">
      <div class="left-sidebar">
        <div class="icon-search">
          <img src="@/assets/img/search_icon.png"  alt="Search Icon" />
          <input type="text" placeholder="search" />
        </div>

        <div class="icon-link">
          <router-link to="social_index">
            <img src="@/assets/img/social_home_icon.png" alt="Home Icon" />
            <span>社群平台首頁</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_collect">
            <img src="@/assets/img/like_icon.png" alt="Saved Posts Icon" />
            <span>收藏貼文</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_follow_list">
             <img src="@/assets/img/followers_icon.png"  alt="Overview Icon" />
            <span>追蹤總覽</span>
          </router-link>
        </div>
      </div>

      <div id="post-container" class="content">
        <div v-for="post in posts" :key="post.username" class="post mb-5">
          <div class="post-header d-flex justify-content-between align-items-center">
            <div class="post-userinfo d-flex align-items-center">
              <img
                src="https://picsum.photos/25"
                alt="User Avatar"
                class="post-avatar rounded-circle"
              />
              <span class="post-username ms-2">{{ post.username }}</span>
            </div>
            <div class="more-options position-relative">
            <!-- 追蹤按鈕 -->
    <button 
      @click="handleToggleFollow(post)" 
      class="follow-button btn"
      :class="{'btn-primary': isFollowing(post.username), 'btn-outline-primary': !isFollowing(post.username)}"
    >
      {{ isFollowing(post.username) ? '已追蹤' : '追蹤' }}
    </button>
              <svg
                aria-label="更多選項"
                class="change"
                fill="currentColor"
                height="24"
                role="img"
                viewBox="0 0 24 24"
                width="24"
                @click="toggleDropdown($event)"
              >
                <title>更多選項</title>
                <circle cx="12" cy="12" r="1.5"></circle>
                <circle cx="6" cy="12" r="1.5"></circle>
                <circle cx="18" cy="12" r="1.5"></circle>
              </svg>
              <ul class="dropdown-menu position-absolute">
                <li><router-link :to="{ name: 'post_edit', params: { id: post.id } }">編輯</router-link></li>
                <li><a href="#" @click="deletePost(post)">刪除</a></li>
                <li><a href="#" @click="sharePost(post)">分享</a></li>
                <li><a href="#" @click="addToCollection(post)">收藏</a></li>
              </ul>
            </div>

          </div>
          <div class="slider_container1 mt-3">
            <div>
              <img :src="post.image" class="l_photo img-fluid" />
            </div>
          </div>
          <ul class="prot mt-3">
            <li>{{ post.description }}</li>
            <li>{{ post.hashtags }}</li>
          </ul>
          <div class="post-time-location d-flex justify-content-left mt-2">
            <span class="post-location">地點：{{ post.location }}</span>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="post-time">時間：{{ post.time }}</span>
          </div>
          <div class="post-actions mt-3 d-flex justify-content-left">
  <button @click="likePost(post)" class="like-button btn btn-outline-primary">讚</button>
  <span>{{ post.likes }}</span>
  <button @click="toggleCommentBox" class="comment-button btn btn-outline-secondary">留言</button>
  <span>{{ post.comments }}</span>
</div>
<div class="comment-section mt-3">
  <!-- 渲染每個留言 -->
  <div v-for="(comment, index) in post.commentList" :key="index" class="comment-content">
    <!-- 顯示用戶頭像 -->
    <img :src="comment.avatar" alt="User Avatar" class="comment-avatar rounded-circle me-2" />
    <!-- 顯示用戶名和留言內容 -->
    <div>
      <span class="fw-bold">{{ comment.username }}</span>
      <p class="comment-text mb-0">{{ comment.content }}</p>
    </div>
  </div>
  
  <!-- 留言輸入框 -->
  <textarea v-model="post.newComment" class="form-control mb-2" placeholder="請輸入留言..."></textarea>
  <button @click="submitComment(post)" class="btn btn-primary">提交留言</button>
</div>

        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      posts: [
        {
          id: 1,
          username: "嗡嗡嗡",
          description: "今日OOTD，鄰家妹妹vs帥氣姐姐，更喜歡哪個~~😍",
          hashtags: "#OOTD #帥氣 #甜美",
          location: "中原大學",
          time: "2024-04-18",
          image: require('@/assets/img/post_01.jpg'),
          likes: 12,
          comments: 3,
          newComment: "",
          commentList: [
            { username: "用戶A", content: "兩個都超愛 ❤️", avatar: "https://picsum.photos/25?random=1" },
            { username: "用戶B", content: "小孩子才做選擇，我兩個都要！", avatar: "https://picsum.photos/25?random=2" },
            { username: "用戶C", content: "怎麼可以這麼會搭😍", avatar: "https://picsum.photos/25?random=3" },
          ],
          isFollowing: false,  // 初始狀態為未追蹤 // 新增留言列表屬性
        },
        {
          id: 2,
          username: "哇哈哈",
          description: "今天天氣真好，出門散步拍了些美照。",
          hashtags: "#散步 #美照 #好心情",
          location: "台北市",
          time: "2024-04-17",
          image: "https://picsum.photos/300/200?random=1",
          likes: 8,
          comments: 5,
          newComment: "", // 新增一个属性用于存储新留言
          commentList: [
  { username: "用戶A", content: "照片好美！陽光真的讓人心情大好呢！", avatar: "https://picsum.photos/25?random=1" },
  { username: "用戶B", content: "看起來好放鬆，真的很適合散步的天氣～", avatar: "https://picsum.photos/25?random=2" },
  { username: "用戶C", content: "這樣的日子就是要好好享受戶外活動啊！😍", avatar: "https://picsum.photos/25?random=3" },
  { username: "用戶D", content: "台北今天的天氣確實很棒！拍得真好！📸", avatar: "https://picsum.photos/25?random=4" },
  { username: "用戶E", content: "哇，風景美麗，人心情更美～❤️", avatar: "https://picsum.photos/25?random=5" },
          ],
          isFollowing: false,  // 初始狀態為未追蹤 
        },
        {
          id: 3,
          username: "小明",
          description: "剛完成了一幅新畫作，分享給大家看看。",
          hashtags: "#畫作 #藝術 #分享",
          location: "高雄市",
          time: "2024-04-16",
          image: "https://picsum.photos/300/200?random=2",
          likes: 15,
          comments: 7,
          newComment: "", // 新增一个属性用于存储新留言
          commentList: [
  { username: "用戶A", content: "這幅畫好有創意，顏色搭配得真棒 🎨", avatar: "https://picsum.photos/25?random=6" },
  { username: "用戶B", content: "哇，藝術家！這幅畫的細節太美了，厲害！", avatar: "https://picsum.photos/25?random=7" },
  { username: "用戶C", content: "喜歡你的風格，這次的作品也很棒！💖", avatar: "https://picsum.photos/25?random=8" },
  { username: "用戶D", content: "感覺好有故事的一幅畫，真想多了解背後的靈感～", avatar: "https://picsum.photos/25?random=9" },
  { username: "用戶E", content: "每次看到你的作品都讓人眼前一亮，繼續加油！💪", avatar: "https://picsum.photos/25?random=10" },
  { username: "用戶F", content: "這畫充滿了獨特的情感，能感受到你的用心！👍", avatar: "https://picsum.photos/25?random=11" },
  { username: "用戶G", content: "每次看到你的作品，都覺得很震撼！這幅畫真的很有層次感～👏", avatar: "https://picsum.photos/25?random=12" },
],
isFollowing: false,  // 初始狀態為未追蹤

        },
      ],
    };
  },
  mounted() {
    /*let counter = 1;
    setInterval(() => {
      document.getElementById("radio" + counter).checked = true;
      counter++;
      if (counter > 4) {
        counter = 1;
      }
    }, 5000);*/

    document.addEventListener("click", (event) => {
      document.querySelectorAll(".dropdown-menu").forEach((menu) => {
        if (!event.target.closest(".more-options")) {
          menu.classList.remove("show");
        }
      });
    });
  },
computed: {
    ...mapGetters('follow', ['isFollowing'])
    },
  
  methods: {
    ...mapActions('follow', ['followUser', 'unfollowUser']),
    
    // 處理追蹤按鈕點擊
    handleToggleFollow(post) {
      const isFollowing = this.isFollowing(post.username);
      if (isFollowing) {
        // 如果已追蹤，則取消追蹤
        this.unfollowUser(post.username);
      } else {
        // 如果未追蹤，則進行追蹤
        this.followUser({ username: post.username });
      }
    },


    // 獲取貼文列表
    async fetchPosts() {
      try {
        const response = await http.get('/api/posts');
        this.posts = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    // 跳轉到編輯頁面
    editPost(postId) {
      this.$router.push({ name: 'post_edit', params: { postId } }); // Pass postId as a parameter} });
    },
    deletePost(post) {
  // 使用 confirm 彈確認框，讓使用者確認是否要刪除
  const confirmation = confirm('確定要刪除這則貼文嗎？');

  // 如果使用者確認，就刪除貼文
  if (confirmation) {
    const index = this.posts.indexOf(post);
    if (index !== -1) {
      this.posts.splice(index, 1); // 刪除該貼文
      console.log('貼文已刪除:', post);
    }
  } else {
    console.log('使用者取消刪除操作');
  }
},
    sharePost(post) {
  if (navigator.share) {
    navigator.share({
      title: post.username + '的貼文',
      text: post.description,
      url: window.location.href, // 當前頁面的網址
    })
    .then(() => console.log('貼文已分享'))
    .catch((error) => console.error('分享失敗:', error));
  } else {
    alert('你的瀏覽器不支援分享功能');
  }
},

    toggleDropdown(event) {
      event.currentTarget.nextElementSibling.classList.toggle("show");
    },
    
    toggleCommentBox(event) {
      const commentBox =
        event.currentTarget.parentElement.nextElementSibling;
      commentBox.style.display =
        commentBox.style.display === "none" || !commentBox.style.display
          ? "block"
          : "none";
    },

    likePost(post) {
      // 增加貼文的讚數
      post.likes++;
    },
    created() {
    this.fetchPosts();
  },

    // 正確使用 mapActions
    ...mapActions(['addToCollection']),
  addToCollection(postId) {
    // Use Vuex dispatch, not a direct method call
    this.$store.dispatch('addToCollection', postId);
  },

    /*問題
      抓不到有效token
      會有401 Unauthorized
    */
   
    /* Google 登入並提交留言的整合功能 */
    async handleGoogleLoginAndSubmitComment(response, post) {
      try {
        // 1. 發送 Google 登入請求到後端，並獲取 JWT Token
        const jwtResponse = await axios.post('http://localhost:8000/auth/google/', {
          access_token: response.tokenObj.access_token  // Google OAuth 取得的 access_token
        });

        // 2. 從後端的回應中獲取 JWT Token
        const token = jwtResponse.data.access;
        console.log('JWT Token:', token);

        // 3. 將 JWT Token 保存到 localStorage
        localStorage.setItem('token', token);

        // 4. 檢查留言內容是否為空
        console.log("留言內容:", post.newComment);  // 調試，檢查留言內容
        if (post.newComment.trim() === '') {
          alert('留言不能為空');
          return;
        }

        // 5. 從 localStorage 中讀取保存的 JWT Token
        const storedToken = localStorage.getItem('token');
        console.log("從 localStorage 讀取到的 token:", storedToken);

        if (!storedToken) {
          alert('未找到有效的 token');
          return;
        }

        // 6. 發送提交留言的請求
        const commentResponse = await axios.post('http://localhost:8000/social_platform/comments/', {
          content: post.newComment,  // 留言的內容
          post: post.id,  // 貼文的 ID
        }, {
          headers: {
            'Authorization': `Bearer ${storedToken}`  // 使用 JWT Token
          }
        });

        // 7. 提交成功後的處理
        alert('留言提交成功');
        post.comments++; // 更新本地的留言數量
        post.newComment = '';  // 清空留言框
      } catch (error) {
        console.error("錯誤信息:", error.response ? error.response.data : error.message);
        alert('提交失敗，請重試');
      }
    },

    async submitComment(post) {
      console.log("留言內容:", post.newComment);  // 調試，檢查留言內容
      
      // 檢查留言內容是否為空
      if (post.newComment.trim() === '') {
        alert('留言不能為空');
        return;
      }

      try {
        // 從 localStorage 中獲取 token
        const token = localStorage.getItem('token');  
        console.log("Token:", token);  // 調試以確保 token 是否存在

        // 如果未找到 token，提示用戶
        if (!token) {
          alert('未找到有效的 token');
          return;
        }

        // 發送留言的 POST 請求
        const response = await axios.post('http://localhost:8000/social_platform/comments/', {
          content: post.newComment,  // 留言的內容
          post: post.id,  // 貼文的 ID
        }, {
          headers: {
            'Authorization': `Bearer ${token}`  // 將 token 添加到 Authorization 標頭
          }
        });

        // 提交成功後的處理邏輯
        alert('留言提交成功');
        post.comments++; // 更新本地的留言數量
        post.newComment = '';  // 清空留言框
      } catch (error) {
        // 錯誤處理
        console.error("錯誤信息:", error.response ? error.response.data : error.message);
        alert('提交失敗，請重試');
      }
    },

    /*editPost(post) {
      // 編輯貼文的邏輯
      console.log('編輯貼文:', post);
    },
    
    deletePost(post) {
      // 刪除貼文的邏輯
      console.log('刪除貼文:', post);
    },

    sharePost(post) {
      // 分享貼文的邏輯
      console.log('分享貼文:', post);
    },
    savePostToCollect(post) {
   post.saved = !post.saved;
   if (post.saved) {
      console.log('收藏貼文:', post);
   } else {
      console.log('取消收藏:', post);
   }
},*/
  },

};
</script>

<style scoped>
.main-content {
  width: 90%;
  position: relative;
  display: flex;
  flex-direction: column;
}

.post {
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  max-width: 600px;
  background-color: #fff;
  color: rgb(8, 8, 8);
  text-align: left;
}

.post-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.post-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.post-username {
  font-size: 1.2em;
  padding: 10px;
}

.post-userinfo {
  display: flex;
  align-items: center;
}

.more-options {
  position: relative;
}

.more-options svg {
  cursor: pointer;
}

.dropdown-menu {
  display: none;
  position: absolute;
  right: 0;
  top: 30px;
  background: white;
  border: 1px solid #dbdbdb;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 3px;
  overflow: hidden;
  z-index: 1;
  white-space: nowrap;
}

.dropdown-menu.show {
  display: block;
}

.dropdown-menu li {
  list-style: none;
}

.dropdown-menu li a {
  display: block;
  padding: 10px 20px;
  text-decoration: none;
  color: black;
}

.dropdown-menu li a:hover {
  background-color: #f0f0f0;
}

.follow-button {
  margin-right: 20px;
}

.post img {
  display: block;
  margin: 0 auto;
}

.prot {
  list-style: none;
  padding: 0;
  text-align: left;
  margin-bottom: 20px;
  margin: 10px 0;
}

.prot li {
  margin: 10px 0;
}

.post-actions {
  display: flex;
  justify-content: flex-start;
  gap: 10px;
  margin-top: 20px;
  align-items: center;
}

.post-actions button {
  background-color: #f0a9a9;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: white;
}

.post-actions button:hover {
  background-color: #e09393;
}

.slider_container1 img {
  max-width: 100%;
  border-radius: 8px;
}

.comment-section {
  display: none;
  margin-top: 10px;
}

.comment-section textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.comment-section button {
  margin-top: 10px;
}

.comment-section button {
  background-color: #f0a9a9;
  color: white; /* 白色文字 */
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.comment-section button:hover {
  background-color: #e09393; /* 當鼠標懸停時，顏色變深 */
}

.comment-avatar {
  width: 40px;  /* 增加頭像大小 */
  height: 40px; /* 同樣增加高度來匹配寬度 */
  border-radius: 50%;
  margin-right: 10px; /* 調整頭像和文字之間的距離 */
}

.comment-content {
  display: flex;
  flex-direction: row; /* 確保是水平排列 */
  align-items: flex-start; /* 頭像和文字對齊 */
  justify-content: flex-start; /* 確保所有內容靠左 */
  text-align: left; /* 留言內容靠左對齊 */
  margin-bottom: 10px; /* 調整上下間距 */
  width: 100%; /* 確保內容不溢出 */
}

.comment-content div {
  flex: 1; /* 讓留言內容占據剩餘空間 */
}

.comment-text {
  text-align: left; /* 留言文字靠左對齊 */
  margin: 0; /* 去掉多餘的上下間距 */
  white-space: pre-wrap; /* 保持換行格式 */
}

@media screen and (max-width: 800px) {
  .slider {
    margin: 20px auto;
  }

  .slide img {
    border-radius: 20px;
  }

  .post {
    padding: 10px;
    margin: 10px 0;
    border-radius: 20px;
  }

  .post-actions button {
    padding: 5px 10px;
  }
}


/* 确保左侧边栏在大屏幕时显示 */
.left-sidebar {
  width: 200px;
  background-color: #f0f0f0;
  padding: 20px;
  position: fixed;
  top: 70px;
  left: 0;
  height: calc(100% - 120px);
  overflow-y: auto;
  z-index: 10;
  transition: all 0.3s ease;
}


.left-sidebar .icon-search,
.left-sidebar .icon-link {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.left-sidebar .icon-search img,
.left-sidebar .icon-link img {
  margin-right: 10px;
  width: 30px;
  height: 30px;
  transition: all 0.3s ease;
}

.left-sidebar .icon-search input {
  flex: 1;
}

.left-sidebar .icon-link a {
  text-decoration: none;
  color: var(--primary-text-color);
  font-weight: 600;
  transition: all 0.3s ease;
  
}

/* 小屏幕样式 */
@media (max-width: 768px) {
  .left-sidebar {
    width: 100%;
    position: fixed;
    top: 60px;
    left: 0;
    height: 60px;
    display: flex;
    justify-content: space-around;
    padding: 15px;
    background-color: var(--header-footer-bg-color);
  }

  .main-content {
    margin-top: 90px;
  }

  .left-sidebar .icon-search {
    display: none; /* 隐藏搜索栏位 */
  }

  .left-sidebar .icon-link {
    flex-direction: column;
    align-items: center;
    margin-bottom: 0;
  }

  .left-sidebar .icon-link span {
    display: none; /* 隐藏文字 */
  }

  .left-sidebar .icon-link img {
    margin-right: 0;
    width: 40px;
    height: 40px;
  }
}


.left-sidebar .icon-search input {
  width: 100px; /* 设置搜索框的宽度 */
  height: 30px; /* 设置搜索框的高度 */
  padding: 5px; /* 调整内边距 */
  font-size: 14px; /* 调整字体大小 */
  border-radius: 10px; /* 调整圆角 */
  border: 1px solid #ccc; /* 设置边框 */
}

/* 在小屏幕时也可以相应调整搜索框大小 */
@media (max-width: 768px) {
  .left-sidebar .icon-search input {
    width: 100px; /* 调整小屏幕时的宽度 */
    height: 25px; /* 调整小屏幕时的高度 */
    font-size: 12px; /* 调整小屏幕时的字体大小 */
  }
}

</style>
