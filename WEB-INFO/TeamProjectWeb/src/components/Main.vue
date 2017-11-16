<style lang="less">
  @import "./main.less";
</style>
<style scoped>
  .layout {
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
  }

  .layout-breadcrumb {
    padding: 10px 15px 0;
  }

  .layout-content {
    min-height: 520px;
    margin: 15px;
    overflow: hidden;
    background: #fff;
    border-radius: 4px;
  }

  .layout-content-main {
    padding: 10px;
  }

  .layout-copy {
    text-align: center;
    padding: 10px 0 20px;
    color: #9ea7b4;
  }

  .layout-menu-left {
    background: #464c5b;
  }

  .layout-header {
    height: 60px;
    background: #fff;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .1);
  }

  .layout-logo-left {
    width: 90%;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    margin: 15px auto;
  }

  .layout-ceiling-main a {
    color: #9ba7b5;
  }

  .layout-hide-text .layout-text {
    display: none;
  }

  .ivu-col {
    transition: width .2s ease-in-out;
  }
</style>
<template>
  <div class="layout" :class="{'layout-hide-text': spanLeft < 5}">
    <Row type="flex">
      <Col :span="spanLeft" class="layout-menu-left">
      <Menu active-name="1-2" theme="dark" width="auto" :open-names="['1']">
        <div class="layout-logo-left"></div>
        <router-link to="/">
          <Menu-item name="1">
            <Icon type="navicon-round" :size="iconSize"></Icon>
            <span class="layout-text">控制台</span>
          </Menu-item>
        </router-link>
        <Submenu name="2">
          <template slot="title">
            <Icon type="ios-keypad" :size="iconSize"></Icon>
            <span class="layout-text">排名</span>
          </template>
          <router-link :to="{path: '/allRank'}"><Menu-item name="2-1">总体排名</Menu-item></router-link>
          <router-link :to="{path: '/oneRank'}"><Menu-item name="2-2">单科排名</Menu-item></router-link>
        </Submenu>
        <router-link :to="{path: '/details'}">
        <Menu-item name="3">
          <Icon type="ios-analytics" :size="iconSize"></Icon>
          <span class="layout-text">详情</span>
        </Menu-item>
        </router-link>
      </Menu>
      </Col>
      <Col :span="spanRight">
      <div class="main-header">
        <div class="navicon-con">
          <Button type="text" @click="toggleClick">
            <Icon type="navicon" size="32"></Icon>
          </Button>
        </div>
        <div class="header-middle-con">
          <div class="main-breadcrumb">
            <span style="font-size:20px">学生成绩管理平台</span>
          </div>
        </div>
        <div class="header-avator-con">
          <div class="user-dropdown-menu-con">
            <Row type="flex" justify="end" align="middle" class="user-dropdown-innercon">
              <Dropdown transfer trigger="click" @on-click="handleClickUserDropdown">
                <a href="javascript:void(0)">
                  <span class="main-user-name">{{ userName }}</span>
                  <Icon type="arrow-down-b"></Icon>
                </a>
                <DropdownMenu slot="list">
                  <DropdownItem name="loginout" divided>退出登录</DropdownItem>
                </DropdownMenu>
              </Dropdown>
              <Avatar :src="avatorPath" style="background: #619fe7;margin-left: 10px;"></Avatar>
            </Row>
          </div>
        </div>
      </div>
      <div class="layout-content">
        <div class="layout-content-main">
          <router-view></router-view>
        </div>
      </div>
      <div class="layout-copy">
        2011-2016 &copy; TalkingData
      </div>
      </Col>
    </Row>
  </div>
</template>
<script>
  import Cookies from 'js-cookie'

  export default {
    data () {
      return {
        spanLeft: 5,
        spanRight: 19,
        userName: ''
      }
    },
    computed: {
      iconSize () {
        return this.spanLeft === 5 ? 14 : 24
      },
      avatorPath () {
        return localStorage.avatorImgPath
      }
    },
    mounted () {
      this.userName = Cookies.get('user')
    },
    methods: {
      toggleClick () {
        if (this.spanLeft === 5) {
          this.spanLeft = 2
          this.spanRight = 22
        } else {
          this.spanLeft = 5
          this.spanRight = 19
        }
      },
      handleClickUserDropdown (name) {
        if (name === 'loginout') {
          // 退出登录
          Cookies.remove('user')
          Cookies.remove('password')
          Cookies.remove('hasGreet')
          Cookies.remove('access')
          this.$router.push({
            name: 'login'
          })
        }
      }
    }
  }
</script>
