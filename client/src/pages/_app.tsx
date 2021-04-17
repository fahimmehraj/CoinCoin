import NavigationBar from '../components/navbar'

import type { AppProps } from 'next/app'

import '../styles/globals.css'
import Footer from '../components/Footer'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <div className="relative h-screen bg-gray-100">
      <NavigationBar />
      <Component {...pageProps} />
      <Footer />
      </div>
  )
}

export default MyApp
