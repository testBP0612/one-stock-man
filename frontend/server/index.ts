import mongoose from 'mongoose';
import type { Nitro } from 'nitropack';

export default async (_nitroApp: Nitro) => {
	const config = useRuntimeConfig();
	const mongoUriFromEnv = config.mongodbUri;

	if (!mongoUriFromEnv) {
		// ... 錯誤處理 ...
		throw new Error('MONGO_CONNECTION_STRING is not defined');
	}

	try {
		if (mongoose.connection.readyState !== 1) {
			await mongoose.connect(mongoUriFromEnv, {
				dbName: 'stock_gifts',
			});
			console.log('MongoDB connected successfully to database specified in URI.');
		}
	} catch (error) {
		console.error('Error connecting to MongoDB:', error);
	}
};
