import postcss from 'rollup-plugin-postcss';

export default {
	  input: 'src/main.js',
	  plugins: [
		   postcss(),
		    ],
	  output: {
		      file: 'dist/bundle.js',
		      format: 'iife',
		      sourcemap:  process.env.BUILD === 'development',
		    },
};
