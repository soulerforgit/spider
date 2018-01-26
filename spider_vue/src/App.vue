<template>

    <!--<codemirror v-model="code" :options="cmOptions"></codemirror>-->
    <div>
    <!-- or to manually control the datasynchronization（或者手动控制数据流，需要像这样手动监听changed事件） -->
      <codemirror ref="myCm"
                  :value="code"
                  :options="cmOptions"
                  @ready="onCmReady"
                  @focus="onCmFocus"
                  @input="onCmCodeChange">
      </codemirror>
      <div style="width:540px;height:440px;">
        <iframe src ="http://www.xiami.com/album/8I2Cfte446b?spm=a1z1s.3521865.1997177565.2.HvKjBN&from=searchsubject" width="100%" height="100%" scrolling="yes">
          <p>Your browser does not support iframes.</p>
        </iframe>

      </div>
    </div>

</template>

<script>
  import { codemirror } from 'vue-codemirror'

  // require styles
  import 'codemirror/lib/codemirror.css'
  import 'codemirror/lib/codemirror.js'

  // language
  import 'codemirror/mode/python/python.js'

  // require active-line.js
  import'codemirror/addon/selection/active-line.js'
  // closebrackets
  import'codemirror/addon/edit/closebrackets.js'

  // theme css
  import 'codemirror/theme/base16-light.css'

  // keyMap
  import'codemirror/mode/clike/clike.js'
  import'codemirror/addon/edit/matchbrackets.js'
  import'codemirror/addon/comment/comment.js'
  import'codemirror/addon/dialog/dialog.js'
  import'codemirror/addon/dialog/dialog.css'
  import'codemirror/addon/search/searchcursor.js'
  import'codemirror/addon/search/search.js'
  import'codemirror/keymap/sublime.js'


  // require more codemirror resource...

  // component
  export default {
    data () {
      return {
        code: 'import requests',
        cmOptions: {
          // codemirror options
          tabSize: 4,
          mode: 'text/x-python',
          theme: 'base16-light',
          lineNumbers: true,
          styleActiveLine: true,
          autoCloseBrackets: true,
          line: true,
          keyMap: "sublime"

          // more codemirror options, 更多 codemirror 的高级配置...
        }
      }
    },
    methods: {
      onCmReady(cm) {
        console.log('the editor is readied!', cm)
      },
      onCmFocus(cm) {
        console.log('the editor is focus!', cm)
      },
      onCmCodeChange(newCode) {
        console.log('this is new code', newCode)
        this.code = newCode
      }
    },
    computed: {
      codemirror() {
        return this.$refs.myCm.codemirror
      }
    },
    mounted() {
      console.log('this is current codemirror object', this.codemirror)
      // you can use this.codemirror to do something...
    },
    components: {
      codemirror
    }
  }
</script>

