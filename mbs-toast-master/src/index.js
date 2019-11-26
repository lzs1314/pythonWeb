import Toast from './component'
import { iconsMap, titleMap } from './config'
const ToastPlugin = {
  install (Vue, options = {}) {
    const ToastConstructor = Vue.extend(Toast)
    Vue.prototype.$toast = toast

    function buildProps (args) {
      let props = {}
      props.message = args[0]
      // 类型
      if (args[1] && args[1].type) props.type = args[1].type
      else props.type = 'info'
      // 位置
      if (args[1] && args[1].position) props.position = args[1].position
      else props.position = 'topCenter'
      // 默认关闭时间
      if (args[1] && args[1].closeTime) props.closeTime = args[1].closeTime
      else props.closeTime = 3
      // 自动关闭
      if (args[1] && Object.prototype.hasOwnProperty.call(args[1], 'autoClose')) props.autoClose = args[1].autoClose
      else props.autoClose = true
      // 默认宽度
      if (args[1] && Object.prototype.hasOwnProperty.call(args[1], 'width')) props.width = args[1].width
      else props.width = 300
      // 默认高度
      if (args[1] && Object.prototype.hasOwnProperty.call(args[1], 'height')) props.height = args[1].height
      else props.height = 80
      props.title = titleMap[props.type]
      props.icon = iconsMap[props.type]
      props.callback = args[1] && args[1].callback ? args[1].callback : null
      return props
    }

    function toast () {
      if (!arguments[0]) return
      const propsData = buildProps(arguments)
      const instance = new ToastConstructor({ propsData })
      document.body.appendChild(instance.$mount().$el)
    }
  }
}

export default ToastPlugin
