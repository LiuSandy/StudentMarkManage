<template>
  <div>
    <Input v-model="value" icon="search" placeholder="请输入学号" style="width: 200px" @on-change="_getAllRank"></Input>
    <br><br>
    <Table border :context="self" :columns="columns1" :data="data1"></Table>
    <br>
    <Page :total="Number(total)" :current="1" show-elevator @on-change="changePage"></Page>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        total: '',
        value: '',
        allRank: [],
        alldata: [],
        self: this,
        columns1: [
          {
            title: '学号',
            key: 'studentId'
          },
          {
            title: '姓名',
            key: 'name'
          },
          {
            title: '总分',
            key: 'allScore'
          },
          {
            title: '排名',
            key: 'grade'
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
                }, '查看'),
                h('Button', {
                  props: {
                    type: 'info',
                    size: 'small',
                    icon: 'stats-bars'
                  },
                  on: {
                    click: () => {
                      this.$router.push({name: 'saleShow', params: {id: `${this.data1[params.index].sale_nbr}`}})
                    }
                  }
                }, '详情')
              ])
            }
          }
        ],
        data1: []
      }
    },
    mounted () {
      this._getAllRank()
    },
    methods: {
      _getAllRank () {
        this.$http.get('/getAllRank').then(response => {
          this.total = response.data.length
          let temp = []
          if (this.value !== '') {
            let studentId = this.value
            let index = 0
            index = this.$_.findIndex(response.data, function (chr) {
              return chr[0] === Number(studentId)
            })
            temp = response.data[index]
          } else {
            temp = response.data
          }
          let tempData = []
          for (let i in temp) {
            let item = {
              studentId: temp[i][0],
              name: temp[i][1],
              allScore: temp[i][2],
              grade: Number(i) + 1
            }
            tempData.push(item)
            if (tempData.length === 10) {
              this.alldata.push(tempData)
              tempData = []
            }
          }
          this.data1 = this.alldata[0]
        })
      },
      show (index) {
        this.$Modal.info({
          title: '学生成绩详情',
          content: `sale_nbr：${this.data1[index].sale_nbr}<br>cnt：${this.data1[index].cnt}<br>round：${this.data1[index].round}<br>in_degree：${this.data1[index].in_degree}<br>out_degree：${this.data1[index].out_degree}<br>page_rank：${this.data1[index].PageRank}`
        })
      },
      changePage (event) {
        if (this.alldata.length >= event) {
          this.data1 = this.alldata[event - 1]
        }
      }
    }
  }
</script>
