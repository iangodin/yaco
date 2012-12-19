
EnableModule( "lang_cpp" )
EnableModule( "unittest" )

BuildConfig( "build", "Build", default=True )
BuildConfig( "debug", "Debug" )
BuildConfig( "release", "Release" )

if sys.platform.startswith( 'linux' ):
    sys.stdout.write( "Configuring for linux...\n" )
    generator.DefineGlobal( 'CC', FindExecutable( "gcc" ) )
    generator.DefineGlobal( 'CXX', FindExecutable( "g++" ) )
    generator.DefineGlobal( 'LD', FindExecutable( "g++" ) )
    generator.DefineGlobal( 'CXXFLAGS', [ "-std=c++0x" ] )
    generator.DefineGlobal( 'AR', FindExecutable( "ar" ) )
    generator.DefineGlobal( 'WARN', [ "-Wall" ] )
#    generator.DefineGlobal( 'LDFLAGS', [ "-lc++" ] )
#    generator.DefineGlobal( 'CC', FindExecutable( "clang" ) )
#    generator.DefineGlobal( 'CXX', FindExecutable( "clang++" ) )
#    generator.DefineGlobal( 'LD', FindExecutable( "clang++" ) )
#    generator.DefineGlobal( 'CXXFLAGS', [ "-std=c++11", "-stdlib=libc++" ] )
#    generator.DefineGlobal( 'AR', FindExecutable( "ar" ) )
#    generator.DefineGlobal( 'WARN', [ "-Weverything", "-Wno-c++98-compat" ] )
#    generator.DefineGlobal( 'LDFLAGS', [ "-lc++" ] )

if sys.platform.startswith( 'darwin' ):
    sys.stdout.write( "Configuring for OS/X...\n" )
    generator.DefineGlobal( 'CC', FindExecutable( "clang" ) )
    generator.DefineGlobal( 'CXX', FindExecutable( "clang++" ) )
    generator.DefineGlobal( 'LD', FindExecutable( "clang++" ) )
    generator.DefineGlobal( 'CXXFLAGS', [ "-std=c++11", "-stdlib=libc++" ] )
    generator.DefineGlobal( 'AR', FindExecutable( "ar" ) )
    generator.DefineGlobal( 'WARN', [ "-Weverything", "-Wno-c++98-compat" ] )
    generator.DefineGlobal( 'LDFLAGS', [ "-lc++" ] )

Include( "include" )
