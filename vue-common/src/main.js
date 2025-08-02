import { createApp } from 'vue'
import SectionHelloWorld from './components/SectionHelloWorld.vue'

const componentMap = {
  'section-hello-world': SectionHelloWorld,
}

document.addEventListener('DOMContentLoaded', () => {
  const sectionEls = document.querySelectorAll('[id^="section-"]')

  sectionEls.forEach((el) => {
    const id = el.id
    const component = componentMap[id]
    if (component) {
      const props = Object.fromEntries(Object.entries(el.dataset))
      createApp(component, props).mount(el)
    } else {
      console.warn(`🔍 No Vue component mapped for id="${id}"`)
    }
  })
})
