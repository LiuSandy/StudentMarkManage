<template>
  <div>
    <Input v-model="value" icon="search" placeholder="请输入学号" style="width: 200px" @on-change="_getDetail"></Input>
    <br><br>
    <Table border :context="self" :columns="columns" :data="data"></Table>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        total: '',
        value: '',
        allInfo: [],
        self: this,
        columns: [
          {
            title: '学号',
            key: 'studentId'
          },
          {
            title: '姓名',
            key: 'name'
          },
          {
            title: 'C语言',
            key: 'C'
          },
          {
            title: 'Python',
            key: 'Python'
          },
          {
            title: '安卓',
            key: 'Android'
          },
          {
            title: 'Linux',
            key: 'Linux'
          },
          {
            title: '网络',
            key: 'Network'
          },
          {
            title: '快速建站',
            key: 'Net'
          },
          {
            title: '操作',
            key: 'action',
            width: 150,
            align: 'center',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.show(params.index)
                    }
                  }
                }, '查看')
              ])
            }
          }
        ],
        data: []
      }
    },
    mounted () {
      this._getDetail()
    },
    methods: {
      _getDetail () {
        let studentId = ''
        if (this.value !== '') {
          studentId = this.value
        } else {
          this.data = []
          return
        }
        this.$http.get('/getDetail', {params: {'q': studentId}}).then(response => {
          let detail = response.data[0].detailScore
          this.allInfo = response.data[0]
          let item = {
            studentId: this.allInfo.studentId,
            name: this.allInfo.name,
            C: detail['C语言'][0],
            Python: detail['Python'][0],
            Android: detail['安卓'][0],
            Linux: detail['Linux'][0],
            Network: detail['网络'][0],
            Net: detail['快速建站'][0]
          }
          this.data.push(item)
        })
      },
      show (index) {
        this.$Modal.info({
          title: '成绩信息',
          content: `总分：${this.allInfo.totalScore}<br>排名：${this.allInfo.totalRanking}<br>`
        })
      }
    }
  }
</script>
