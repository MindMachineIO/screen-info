{
  'targets': [{
    "includes": [
		"auto.gypi"
	],



    'conditions': [
      ['OS == "mac"', {
	    'sources': [
	      'src/macos-screen.mm',
        'src/common.cc'
	    ],
        'include_dirs': [
          'System/Library/Frameworks/CoreFoundation.Framework/Headers',
          'System/Library/Frameworks/Carbon.Framework/Headers',
          'System/Library/Frameworks/ApplicationServices.framework/Headers',
          'System/Library/Frameworks/OpenGL.framework/Headers',
        ],
        'link_settings': {
          'libraries': [
            '-framework Carbon',
            '-framework CoreFoundation',
            '-framework ApplicationServices',
            '-framework OpenGL'
          ]
        }
      }],

      ['OS == "linux"', {
        'link_settings': {
          'libraries': [
            '-lX11',
          ]
        },

        'sources': [
          'src/linux-screen.cc',
          'src/common.cc'
        ]
      }],

      ["OS=='win'", {
        'defines': ['IS_WINDOWS'],
        'sources': [
          'src/windows-screen.cc',
          'src/common.cc'
        ]
      }]
    ],


  }],
	"includes": [
		"auto-top.gypi"
	]
}