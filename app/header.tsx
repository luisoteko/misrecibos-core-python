// Make a pretty header using tailwindcss
export default function Header() {
  return (
    <header>
      <nav className="bg-gray-800">
        <div className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
          <div className="relative flex items-center justify-between h-16">
            <div className="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
              <div className="flex-shrink-0 flex items-center">
                <span className="text-white text-2xl font-bold tracking-tight font-mono sm:text-3xl sm:tracking-tighter sm:font-extrabold">
                  MisRecibos
                </span>
              </div>
              <div className="hidden sm:block sm:ml-6">
                <div className="flex space-x-4">
                  <a href="/" className="bg-gray-900 text-white px-3 py-2 rounded-md text-sm font-medium">Dashboard</a>
                </div>
              </div>
            </div>
            <div className="absolute right-0 flex items-center pr-2 sm:static sm:inset-auto sm:pr-0">
              <button className="bg-gray-800 p-1 rounded-full text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                <span className="sr-only">View notifications</span>
                <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z
                  " />
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 20a2 2 0 01-2 2H5a2 2 0 01-2-2v-1
                  3" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </nav>
    </header>
  )
}