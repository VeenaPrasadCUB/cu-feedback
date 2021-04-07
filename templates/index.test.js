import { fireEvent, getByText } from '@testing-library/dom'
import '@testing-library/jest-dom/extend-expect'
import { JSDOM } from 'jsdom'
import fs from 'fs'
import path from 'path'

const html = fs.readFileSync(path.resolve(__dirname, './index.html'), 'utf8');

let dom
let container
describe('index.html', () => {
  beforeEach(() => {
    dom = new JSDOM(html, { runScripts: 'dangerously' })
    container = dom.window.document.body
  })

  it('renders a heading element', () => {
    expect(container.querySelector('h1')).not.toBeNull()
  })

   it('renders a title ', () => {
      expect(getByText(container, 'CU FEEDBACK')).toBeInTheDocument()
  })

  it('renders google sign-in wrapper', () => {
      expect(container.querySelectorAll('gSignInWrapper')).not.toBeNull()
  })

    it('renders a login element', () => {
       expect(getByText(container, 'LOGIN:')).toBeInTheDocument()
  })
})